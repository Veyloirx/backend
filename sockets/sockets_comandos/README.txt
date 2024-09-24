
Este proyecto implementa una comunicación cliente-servidor utilizando sockets en Python, 
donde el cliente puede enviar comandos al servidor para interactuar con los archivos en el directorio del servidor. 
A continuación se describen los componentes principales:

1. Archivo del Servidor (server.py):


El servidor acepta múltiples clientes mediante el uso de hilos.
Funciona escuchando comandos enviados por los clientes y responde de acuerdo con las solicitudes.

Comandos disponibles:
lsFiles: Lista todos los archivos dentro de un directorio llamado Files en la ruta del servidor.

get <archivo.extension>: 
Envía el archivo solicitado al cliente si este se encuentra dentro de la carpeta Files.
Lo guarda dentro de una carpeta 'download', si existe, de no existir, la crea y lo guarda. 



2. Archivo del Cliente (client.py):


El cliente se conecta al servidor a través de una conexión de socket.
El cliente puede interactuar con el servidor utilizando los comandos mencionados:
lsFiles: Solicita la lista de archivos en el servidor.
get <archivo>: Solicita la descarga de un archivo específico del servidor.
Cuando se recibe un archivo desde el servidor, el cliente lo guarda en una carpeta llamada download, que se crea automáticamente en la ruta local del cliente si no existe.
El archivo recibido se guarda bajo el nombre archivo_recibido dentro de esta carpeta.
