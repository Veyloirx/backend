import socket
import sys
import threading
import pickle
import os

class Cliente:

    def __init__(self, host="localhost", port=7003):
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
            if msg.startswith('lsFiles') or msg.startswith('get'):
                self.send_msg(msg)
            elif msg == 'salir':
                self.sock.close()
                sys.exit()
            else:
                print("Comando no reconocido.")

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(4096)
                if data:
                    response = pickle.loads(data)
                    if isinstance(response, list):
                        print("Archivos disponibles:")
                        for file in response:
                            print(file)
                    elif isinstance(response, bytes):
                        self.save_file(response)
                    else:
                        print(f"Mensaje recibido: {response}")
            except Exception as e:
                print(f"Error al recibir datos: {e}")
                self.sock.close()
                break

    def send_msg(self, msg):
        try:
            self.sock.send(pickle.dumps(msg))
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    def save_file(self, file_data):
        try:
            current_directory = os.getcwd()
            print(f"Directorio actual: {current_directory}")
            
            #DEBO INVESTEGAR ACERCA DE LOS RUTEOS
            download_dir = os.path.join(current_directory, 'download')
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
                print(f"Carpeta 'download' creada en {download_dir}")
            else:
                print(f"Carpeta 'download' ya existe en {download_dir}")

            filepath = os.path.join(download_dir, 'archivo_recibido')
            with open(filepath, 'wb') as f:
                f.write(file_data)
            print(f"Archivo guardado en {filepath}")
        
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    Cliente()

