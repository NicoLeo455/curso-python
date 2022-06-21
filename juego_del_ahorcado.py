from cgi import print_directory
import random
import platform
import os
import time

def limpiar_pantalla():
    time.sleep(0)
    if platform.system() == 'Windows':
        os.system ("cls")


def read(aleatorio):
    words = {}  #agendar las palabras en una agenda y luego usar get para ubicarla con el numero aleatorio que se creara posteriormente con ranInt
    cont = 1
    with open ("./words.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            words[cont]=palabra
            cont +=1
    return words.get(aleatorio)


def filtrar_acentos(palabra):
    palabra = palabra.replace("á","a")
    palabra = palabra.replace("é","e")
    palabra = palabra.replace("í","i")
    palabra = palabra.replace("ó","o")
    palabra = palabra.replace("ú","u")
    palabra = palabra.replace(" ","")
    return palabra    


def guiones(long):
    guiones = []
    for g in range(long-1):
        guiones.append("- ")
    return guiones


def run():
    
    aleatorio = random.randint(1,144)
    palabra = read(aleatorio)
    palabra=filtrar_acentos(palabra)
    long = len(palabra)             #Se saca la longitud de la palabra
    palabra = palabra[:long-1].lower()      #Se pasa a minuscula

    ubicacion = guiones(long)

    limpiar_pantalla()

    #Interface del juego
    print("========= Star Game =========")
    print("\n")
    print("        Hangman Game        ")
    print("You most insert one letter")
    print("\n")
    for u in ubicacion:
        print(u+"",end="")    #guiones
    print("\n")
    


    #Crear crear una lista con todas las letras de la palabra aleatorio 
    #fragmentar la palabra!
    letras=[]
    for y in palabra:    #list comprehension
        letras.append(y) 
    #print(letras)     


    #Elegir la opcion, filtrarla y reemplazarla por los guiones depende su ubicacion
    while True:
        #print(letras)
        #print(ubicacion)
        opcion= input("Inserte una letra: ").lower()
        if opcion.isnumeric() == True or len(opcion) != 1:
            print("Ingrese solo una letra por favor!")
        elif opcion.isalpha():
            for index,value in enumerate(letras):              
                if value == opcion:
                    for u,y in enumerate(ubicacion):
                        if u==index:
                            ubicacion[u]=opcion
                    limpiar_pantalla()        
                    #print(y+"",end="")   #guiones
                    #print(letras)
                    print("========= Start Game =========")
                    print("\n")
                    print("        Hangman Game        ")
                    print("You must insert one letter for start game")
                    print("\n")
                    for y in ubicacion:
                        print(y+"",end="")   #guiones
                    print("\n")
        if letras == ubicacion:
            break
                              
    print("Congratulation, you are win the game")

       
    #necesito comparar la opcion elegida por el usuario y letra por letra de la lista llamada "letras"
    #print(palabra,":",str(aleatorio), " y su logitud es de",str(long-1))

if __name__=="__main__":
    run()

