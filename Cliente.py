# -*- coding: cp1252 -*-
#Importar el módulo socket para abrir el canal de comunicación
import socket

#Función principal
def main():
    
    #Asignar valores a las variables (locales)
    msgFromClient       = "Hola Servidor UDP :)" #Mensaje que enviará
    bytesToSend         = str.encode(msgFromClient)#Pasar el mensaje a bytes
    serverAddressPort   = ("127.0.0.1", 20001)#Dirección y puerto del servidor
    bufferSize          = 1024 #Tamaño del buffer

    #Crear un socket UDP en el lado del cliente
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    #Enviar datos / información al servidor mediante el uso del socket UDP
    UDPClientSocket.sendto(bytesToSend, serverAddressPort) #SENDTO: Enviar mensaje al servidor

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Mensaje del servidor {}".format(msgFromServer[0])
    print(".................................................")
    print(msg)
    print(".................................................")


#Sentencia para que cargue alguna función (MAIN)
if __name__ == "__main__":
    main()
    
