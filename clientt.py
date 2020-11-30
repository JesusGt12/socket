# Importamos las librerias necesarias
import socket
import sys
# Establecemos el tipo de socket/conexion
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
cliente.connect(('127.0.0.1',port))
# Leemos los datos del servidor
print("servidor: ",('127.0.0.1',port))

#text = "cliente conectado!"
cliente.send(("cliente conectado!").encode())
while True:
    
    
    msg=input("-- ")
    if msg != 'salir':
        cliente.send(msg.encode())
        respuesta=cliente.recv(1024)
    else:
            cliente.send("Cliente deconectado".encode())
            cliente.close()#cerramos el socket
            print("cliente desconectado")
            sys.exit()#salimos
        
    print ("--> ", respuesta.decode())

    
