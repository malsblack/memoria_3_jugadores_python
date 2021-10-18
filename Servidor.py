import datetime
from math import ceil
from colorama import *
import os
import socket
import time
import random
import threading

        
def jugar():
    
    cliente.send((Style.BRIGHT+Fore.GREEN+"ES TU TURNO \n\n".center(15," ")).encode("UTF-8"))
    cliente.send((Style.BRIGHT+Fore.WHITE+"ESCOGE El NUMERO DE TARJETA A DESTAPAR..\n").encode("UTF-8"))
    cliente.send((memorama.mandar_tablero+"\n").encode("UTF-8"))
    
    mensaje=cliente.recv(1024)
    respuesta=mensaje.decode("UTF-8")
    respuestas=[]
    
    
    if respuesta in memorama.keys :
                    
        respuestas.append(memorama.tablero.get(respuesta))
        cliente.send((memorama.tablero.get(respuesta)+"\n").encode("UTF-8"))
        cliente.send((Style.BRIGHT+Fore.WHITE+"ESCOGE LA SIGUIENTE TARJETA..\n").encode("UTF-8"))
        cliente.send((memorama.mandar_tablero+"\n").encode("UTF-8"))
        mensaje=cliente.recv(1024)
        respuesta=mensaje.decode("UTF-8")
        respuestas.append(memorama.tablero.get(respuesta))
        
        print(len(respuestas))
        print(respuestas)
        
        if len(respuestas)==2:
            if respuestas[0]==respuestas[1]:
                index_1=list(memorama.tablero.keys())[list(memorama.tablero.values()).index(respuestas[0])]
                memorama.tablero.pop(index_1)
                index_2=list(memorama.tablero.keys())[list(memorama.tablero.values()).index(respuestas[0])]
                memorama.tablero.pop(index_2)
                respuestas.clear()
                memorama.mandar_tablero=str(list(memorama.tablero))
                conexion.scoore=+1
            
                cliente.send((Style.BRIGHT+Fore.GREEN+"ACERTASTE, VUELVE A TIRAR:\n\n".center(15," ")).encode("UTF-8"))
                jugar()
               
            else:
                cliente.send((Style.BRIGHT+Fore.RED+"NO HAS ACERTADO, TURNO DEL JUGADOR\n").encode("UTF-8"))
                
                
                   
        
class juego():
    
    valores=["manzana","arbol","mango","raiz","escuela","niño","niña","maestra","manzana","arbol","mango","raiz","escuela","niño","niña","maestra"]
    random.shuffle(valores)
    keys=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    tablero=dict(zip(keys,valores))
    mandar_tablero=str(list(tablero))
              
        
class jugador():
    def __init__(self,cliente,direccion):
        self.cliente= cliente
        self.id = direccion[1]
        self.scoore=0
 
class hilo(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        semaoro.acquire()
        cliente.send((Style.BRIGHT+Fore.YELLOW+"ESPERANDO A QUE FINALIZEN LOS DEMAS JUGADORES\n").encode("UTF-8"))
        jugar()
        semaoro.release()
        if len(memorama.tablero)==0:
            print(conexion.scoore)
            socket_escuchar.close()
                
                 
            
           

    

#Esto es la portada 
memorama=juego()
init(autoreset=True)
os.system("clear")
print("INSTITUTO POLITECNICO NACIONAL".center(50," "))
print("ESCUELA SUPERIOR DE COMPUTO".center(50," "))
print("APLICACIONES PARA COMUNICACIONES DE RED \n".center(55," "))
print("PRACTICA 2".center(50," "))
print(Style.BRIGHT+Fore.CYAN+"SERVIDOR".center(48," "))
print("\n\nINTRUCCIONES")


#Esto es la creacion del socket 
HOST=str(input("INGRESA EL HOST: "))
PUERTO=int(input("INGRESA EL PUERTO: "))
socket_escuchar=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_escuchar.bind((HOST,PUERTO))
   
#Aqui es las peticiones que va a escuchar, ademas del arreglo donde se guardaran las conexiones
socket_escuchar.listen(3)
conexiones=[]
    
#semaforo
semaoro=threading.Semaphore(1)
    
    
while True:
    cliente, direccion = socket_escuchar.accept()
    if cliente  and direccion:
        cliente.send((Style.BRIGHT+Fore.GREEN+"CONEXION ESTABLECIDA\n".center(50," ")).encode("UTF-8"))
        print(Style.BRIGHT+Fore.GREEN+"SE ESTABLECIO UNA CONEXCION CON: {}".format(direccion))
        conexion = jugador(cliente,direccion)
        cliente.send(((Style.BRIGHT + Fore.WHITE + "SU ID ES: {}\n").format(conexion.id)).encode("UTF-8"))
        conexiones.append(conexion)

        if len(conexiones)<=3:
            print(memorama.tablero)
            cliente.send((Style.BRIGHT+Fore.YELLOW+"ERES EL JUGADOR {}\n").format(len(conexiones)).encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.YELLOW+"BIENVENIDO AL JUEGO DE MEMORIA\n\n".center(15," ")).encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.WHITE+"INSTRUCCIONES:\n\n").encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.WHITE+"1.- INGRESA LA DIFICULTAD \n").encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.WHITE+"2.- DEBERAS ENCONTRAR LAS PAREJAS IGUALES\n".center(25," ")).encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.WHITE+"4.- SI ENCUENTRAS UNA PAREJA PUEDES TIRAR OTRA VEZ\n".center(25," ")).encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.WHITE+"5.- DEBERAS DE INGRESAR PRIMERO UNA COORDENADA Y DESPUES OTRA\n".center(25," ")).encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.WHITE+"6.- SI NO ENCUENTRAS LA PAREJA, SERA TURNO DEL SIGUIENTE JUGADOR\n".center(25," ")).encode("UTF-8"))
            cliente.send((Style.BRIGHT+Fore.GREEN+"7.- DIVIERTETE \n\n\n\n").encode("UTF-8"))
            empezamos=hilo(conexion.id)
            empezamos.start()
                    
                                     
        elif len(conexiones)>3:
            cliente.send((Style.BRIGHT+Fore.RED+"NO DISPONIBLE").encode("UTF-8"))
        
    else:
        cliente.send((Style.BRIGHT+Fore.RED+"CONEXION FALLIDA\n".center(50," ")).encode("UTF-8"))
            
