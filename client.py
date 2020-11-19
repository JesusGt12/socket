# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
sock.connect(('127.0.0.1',port))
# Leemos los datos del servidor
data = sock.recv(4096)
# Cerramos el socket
sock.close()
# Mostramos los datos recibidos
print(data.decode())
