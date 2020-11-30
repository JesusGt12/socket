# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 # Establecemos un puerto de comunicacion
sock.bind(('127.0.0.1',port)) # IP y Puerto de conexion en una Tupla
 
print ("esperando conexiones en el puerto ", port)
# Vamos a esperar que un cliente se conecte
# Mientras tanto el script se va a pausar
sock.listen(1)
# Cuando un cliente se conecte vamos a obtener la client_addr osea la direccion
# obtenemos la conexion, que servira para enviar datos y recibir datos
con, client_addr =  sock.accept()
print ("cliente conectado! ")
text = "HOLA, SOY EL SERVIDOR!" # El texto que enviaremos
con.send(text.encode()) # Enviamos el texto al cliente que se conecte
con.close() # Cerramos la conexion
print ("... ")
print ("cliente desconectadooooo! ")
sock.close() # Cerramos el socket

 
