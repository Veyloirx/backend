import pickle
import socket
import sys
import threading

class Servidor:
    def __init__(self, host="localhost", port=7002):
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(10)
        self.sock.setblocking(False)

        self.aceptar = threading.Thread(target=self.aceptarCon)
        self.procesar = threading.Thread(target=self.procesarCon)

        self.aceptar.daemon = True
        self.aceptar.start()

        self.procesar.daemon = True
        self.procesar.start()

        try:
            while True:
                msg = input('-> ')
                if msg == 'salir':
                    break
        except KeyboardInterrupt:
            pass
        finally:
            self.cerrar_servidor()

    def msg_to_all(self, msg):
        for c in self.clientes:
            try:
                c.sendall(msg)
            except socket.error:
                self.clientes.remove(c)
                c.close()

    def aceptarCon(self):
        print("Aceptar conexiones iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                print(f"Cliente conectado: {addr}")
            except BlockingIOError:
                pass
            except Exception as e:
                print(f"Error en aceptar conexiones: {e}")

    def procesarCon(self):
        print("Procesar conexiones iniciado")
        while True:
            if self.clientes:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            try:
                                deserialized_data = pickle.loads(data)
                                print(f"Mensaje recibido: {deserialized_data}")
                            except pickle.UnpicklingError:
                                print(f"Error al deserializar los datos: {data}")
                            except Exception as e:
                                print(f"Error al procesar los datos: {e}")
                            self.msg_to_all(data)
                    except BlockingIOError:
                        pass
                    except Exception as e:
                        print(f"Error en procesar conexiones: {e}")
                        self.clientes.remove(c)
                        c.close()


    def cerrar_servidor(self):
        print("Cerrando servidor")
        for c in self.clientes:
            c.close()
        self.sock.close()
        sys.exit()

if __name__ == "__main__":
    Servidor()
