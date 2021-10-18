import datetime
from colorama import *
import os
import socket
import time

def iniciar_servidor():
    HOST=str(input("\nINGRESA EL HOST: "))
    PUERTO=int(input("\nINGRESA EL PUERTO: "))
    socket_memoria=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_memoria.connect((HOST,PUERTO))
    os.system("clear")

    
    while True:
        respuesta_conexion=socket_memoria.recv(1024)
        respuesta=respuesta_conexion.decode("UTF-8")
        print(respuesta_conexion.decode("UTF-8"))
        enviar=str(input("RESPUESTA:"))
        socket_memoria.send(enviar.encode("UTF-8"))
        os.system("clear")

        
        
        
        if respuesta=="NO DISPONIBLE":
            socket_memoria.close()
            

    
    socket_memoria.close()
    



def main():
    init(autoreset=True)
    os.system("clear")
    print("INSTITUTO POLITECNICO NACIONAL".center(50," "))
    print("ESCUELA SUPERIOR DE COMPUTO".center(50," "))
    print("APLICACIONES PARA COMUNICACIONES DE RED \n".center(55," "))
    print("PRACTICA 2".center(50," "))
    print(Style.BRIGHT+Fore.CYAN+"CLIENTE".center(48," "))
    print(Style.BRIGHT+Fore.YELLOW+"LISTO PARA INICIAR CONEXION".center(48," "))
    iniciar_servidor()
main()