# -*- coding: cp1252 -*-
#Importar el m�dulo socket para abrir el canal de comunicaci�n
import socket

#Funci�n principal
def main():
    localIP             = "127.0.0.1" #Direcci�n IP del servidor
    localPort           = 20001 #Puerto del servidor
    bufferSize          = 1024 #Tama�o del buffer
    msgFromServer       = "Hola Cliente UDP :)" #Mensaje que enviar� de respuesta
    bytesToSend         = str.encode(msgFromServer) #Pasar el mensaje a bytes

    #Crear un Datagrama Socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    #Bind con la direcci�n y puerto
    UDPServerSocket.bind((localIP, localPort))
    print("El servidor UDP est� escuchando...")


    #Ciclo para que el servidor est� "escuchando"
    while(True):
        
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)#RECVFROM: Recibe una petici�n
        message = bytesAddressPair[0] #Mensaje del Cliente (Bytes)
        address = bytesAddressPair[1] #Direcci�n IP del Cliente (Bytes)

        clientMsg = "Mensaje del cliente:{}".format(message)
        clientIP  = "Direcci� IP del cliente:{}".format(address)

        #Mostrar mensaje y direci�n IP
        print(".................................................")
        print(clientMsg)
        print(clientIP)
        print(".................................................")

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address) #BYTESTOSEND: Lo que regresa al cliente


#Sentencia para que cargue alguna funci�n (MAIN)
if __name__ == "__main__":
    main()
