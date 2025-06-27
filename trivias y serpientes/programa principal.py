#Importacion de funciones
from desarrollo import *


#Desarrollo del juego.
posicion = 15
nombre_jugador = iniciar_juego()
while preguntar_jugar() == "s" and not verificar_cantidad_preguntas(preguntas):
    pregunta = sortear_pregunta(preguntas)
    preguntar(pregunta)
    respuesta = responder()
    correcto = evaluar_respuesta(pregunta,respuesta)
    posicion = avanzar_retroceder(correcto,posicion)
    print(f"posicion actual: {posicion}")
    borrar_preguntas(preguntas,pregunta)
    if verificar_ganador(posicion):
        break
    elif verificar_perdedor(posicion):
        break
    
mostrar_posicion_final(posicion,nombre_jugador)

#Guardado del progreso en un archivo csv
guardar_partida(nombre_jugador,posicion)
