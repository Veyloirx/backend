import socket
import sys
import threading
import pickle

class Cliente:

    def __init__(self, host="localhost", port=7001):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((str(host), int(port)))
            print("Conectado al servidor.")
        except Exception as e:
            print(f"No se pudo conectar al servidor: {e}")
            sys.exit()

        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = input('-> ')
            if msg != 'salir':
                self.send_msg(msg)
            else:
                self.sock.close()
                sys.exit()

    def msg_recv(self):

        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    data = pickle.loads(data)  
                    print(f"Mensaje recibido: {data}")
            except Exception as e:
                print(f"Error al recibir datos: {e}")
                self.sock.close()
                break

    def send_msg(self, msg):
        try:
            self.sock.send(pickle.dumps(msg))  
            print(f"Mensaje enviado: {msg}")
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

if __name__ == "__main__":
    Cliente()
