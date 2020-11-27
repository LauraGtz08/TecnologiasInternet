# -*- coding: cp1252 -*-
#Importar el módulo socket para abrir el canal de comunicación
import socket

#Función principal
def main():
    localIP             = "127.0.0.1" #Dirección IP del servidor
    localPort           = 20001 #Puerto del servidor
    bufferSize          = 1024 #Tamaño del buffer
    msgFromServer       = "Hola Cliente UDP :)" #Mensaje que enviará de respuesta
    bytesToSend         = str.encode(msgFromServer) #Pasar el mensaje a bytes

    #Crear un Datagrama Socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    #Bind con la dirección y puerto
    UDPServerSocket.bind((localIP, localPort))
    print("El servidor UDP está escuchando...")


    #Ciclo para que el servidor esté "escuchando"
    while(True):
        
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)#RECVFROM: Recibe una petición
        message = bytesAddressPair[0] #Mensaje del Cliente (Bytes)
        address = bytesAddressPair[1] #Dirección IP del Cliente (Bytes)

        clientMsg = "Mensaje del cliente:{}".format(message)
        clientIP  = "Direcció IP del cliente:{}".format(address)

        #Mostrar mensaje y direción IP
        print(".................................................")
        print(clientMsg)
        print(clientIP)
        print(".................................................")

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address) #BYTESTOSEND: Lo que regresa al cliente


#Sentencia para que cargue alguna función (MAIN)
if __name__ == "__main__":
    main()
