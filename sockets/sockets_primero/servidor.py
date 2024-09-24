import socket
import threading
import os
import pickle

class Servidor:

    def __init__(self, host="localhost", port=7002):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print(f"Servidor escuchando en {host}:{port}")
        self.clients = []

        while True:
            client, addr = self.sock.accept()
            self.clients.append(client)
            print(f"Conectado a {addr}")
            threading.Thread(target=self.client_handler, args=(client,)).start()

    def client_handler(self, client):
        while True:
            try:
                data = client.recv(1024)
                if data:
                    msg = pickle.loads(data)
                    if msg.startswith('ls'):
                        self.list_files(client)
                    elif msg.startswith('get'):
                        _, filename = msg.split()
                        self.send_file(client, filename)
            except Exception as e:
                print(f"Error: {e}")
                client.close()
                break

    def list_files(self, client):
        files = os.listdir('./Files')
        client.send(pickle.dumps(files))

    def send_file(self, client, filename):
        filepath = os.path.join('./Files', filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as file:
                data = file.read()
                client.send(pickle.dumps(data))
        else:
            client.send(pickle.dumps(f"Error: Archivo {filename} no encontrado."))

if __name__ == "__main__":
    Servidor()
