# Importamos las librerias necesarias
import socket
import threading

# Establecemos el tipo de socket/conexion
clientes=[]
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 # Establecemos un puerto de comunicacion
servidor.bind(('127.0.0.1',port)) # IP y Puerto de conexion en una Tupla
  
print ("esperando conexiones en el puerto ", port)
    # Vamos a esperar que un cliente se conecte
    # Mientras tanto el script se va a pausar
servidor.listen(10)
    # Cuando un cliente se conecte vamos a obtener la direccion
    # obtenemos la conexion, que servira para enviar datos y recibir datos

active,c_addr=servidor.accept()
####
        ######      

while True:
    recibido=active.recv(1024)
    print("-- ",recibido.decode())
    enviar=input("--> ")
    active.send(enviar.encode())
######

active.close()
