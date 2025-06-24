import random
import csv
from preguntas import *


tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]
#print(len(tablero))

def iniciar_juego ():
    """La funcion pide un nombre de usuario para iniciar el jeugo y lo retorna."""
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    return nombre_usuario


def preguntar_jugar(): 
    """Pregunta al usuario si desea jugar, lo verifica y retorna la respuesta."""
    jugar = input("Desea jugar 'Trivia: Serpientes u Escaleras'? (s/n): ")
    while jugar != "s" and jugar != "n":
        jugar = input("ERROR.\n Indique con 's' o 'n': Desea jugar 'Trivia: Serpientes y Escaleras'? (s/n): ")
    return jugar

def sortear_pregunta (preguntas:list):
    """Recibe una lista ed preguntas como parametros. Elige una aleatoriamente y lo guarda en una variable.\n Retorna la variable."""
    pregunta = random.choice(preguntas)
    return pregunta

def preguntar(pregunta):   
    """Recibe una pregunta como paramtero.\n
    Muestra tanto la pregunta como las respuestas posibles y pide elegir una de ellas."""
    #pregunta = random.choice(preguntas)
    print(f"Responda correctamente la siguiente pregunta.\n{pregunta['pregunta']}")
    print(f"Respuestas: \n   Respuesta A- {pregunta['respuesta_a']}.\n   Respuesta B- {pregunta['respuesta_b']}.\n   Respuesta C- {pregunta['respuesta_c']}.")
    
def responder():
    """Pide una respuesta al usuario. La retorna."""
    respuesta = input("Indique la respuesta correcta: ").lower()
    return respuesta

def evaluar_respuesta (pregunta, respuesta):
    """Recibe una pregunta y la respuesta del usuario como parametro.\n
    Compara con la respuesta correcta e indica si acertó o no.\n
    Retorna correcto."""
    correcto = False
    if respuesta == pregunta["respuesta_correcta"]:
        correcto = True
        print("Respuesta correcta!! :)")
    else:
        print("Respuesta incorrecta :(")
    
    return correcto

def avanzar_retroceder (correcto, posicion):     
    """Recibe dos variables como parametro.\n
    Modifica la posicion del jugador segun la variable correcto de la funcion evaluar_respuesta.\n
    Retorna la posicion modificada."""   
    if correcto == True:
        posicion = posicion + 1 + tablero[posicion+1]
    else:
        posicion = posicion - 1 - tablero[posicion-1]
    return posicion

def borrar_preguntas(preguntas:list,pregunta:dict):
     """Recibe la lista de preguntas y el diccionario de  la ultima pregunta.\n
     Elimina la ultima pregunta dada durante el juego para que no se repita."""
     preguntas.remove(pregunta)

def seguir_jugando ():
    """Pregunta al usuario si desea continuar jugando."""
    jugar = input("Desea continuar jugando? (s/n): ").lower()
    while jugar != "s" and jugar != "n":
        jugar = input("ERROR.\nIndique con 's' o 'n'. Desea continuar jugando?: ")

def mostrar_posicion_final (posicion:int, nombre_jugador):
    """Muestra la posicion final del jugador."""
    print(f"Posicion final del jugador {nombre_jugador}: {posicion}")

def verificar_cantidad_preguntas(preguntas:list):
    """Chequea que la cantidad de preguntas restantes no sea cero."""
    if len(preguntas) == 0:
        print("Sobreviviste: No hay mas preguntas!\nFin del juego.")
        return True
    
def verificar_ganador(posicion):
    """Termina el juego en caso de que el jugador llegue a la posicion 30 (ganador)"""
    if posicion == 30:
        print("GANASTE EL JUEGO!")
        return True
    
def verificar_perdedor(posicion):
    """Termina el juego en caso de que el jugador llegue a la posicion 1 (perdedor)"""
    if posicion == 0:
        print("Perdiste el juego. ")
        return True


def guardar_partida (jugador, posicion:int):
    """La funcion recibe el nombre del usuario y su posicion final como parametro.\n
    los guarda y muestra en un archivo aparte."""
    with open ("Puntajes.csv","a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([jugador, posicion])