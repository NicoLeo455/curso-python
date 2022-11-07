import random
import platform
import os
import time


HANG = ['''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/   ''']

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def limpiar_pantalla():
    time.sleep(0.5)
    os.system ("cls")


def hang():
    for i in hang:
        print(i) 


def hangmanpics(k):
    print(HANGMANPICS[k])


def filtrar_acentos(palabra):             ##MODIFICAR
    palabra = palabra.replace("á","a")
    palabra = palabra.replace("é","e")
    palabra = palabra.replace("í","i")
    palabra = palabra.replace("ó","o")
    palabra = palabra.replace("ú","u")
    palabra = palabra.replace(" ","")
    return palabra 


def read(aleatorio):
    words = {}  #agendar las palabras en una agenda y luego usar get para ubicarla con el numero aleatorio que se creara posteriormente con ranInt
    cont = 1
    with open ("./Archivos/words.txt", "r", encoding="utf-8") as f:
        dict_words={index:value for index,value in enumerate(f)}        #dictionary comprehension
    return dict_words.get(aleatorio)


def interfase(g):
    #Interface del juego
    print("========= Star Game =========")
    print("\n")
    print("        Hangman Game        ")
    print("You most insert one letter")
    print("\n")
    for i in g:
        print(i,end="")    #guiones
    print("\n")


def run():
    aleatorio = random.randint(1,144)
    palabra = filtrar_acentos(read(aleatorio))  #Palabra alaeatoria elegida
    long = len(palabra)            #Se saca la longitud de la palabra
    palabra = palabra[:long-1].lower()      #Se pasa a minuscula y se quita \n
    guiones = (long-1) * " -"   ## agregar los guiones a una vaiable nueva llamada "ubicacion"
    
    limpiar_pantalla()
    interfase(guiones)

    palabra_long = len(guiones.replace(" ",""))   
    guiones = list(guiones.replace(" ",""))
    count = 0
    vidas = -6

    while True:
        print("Usted tiene " + str(-vidas) + " vidas!")
        vueltas = 0
        hangmanpics(vidas)
        opcion = input("Insert a letter: ")
        for i,y in enumerate(palabra):  
            if opcion == y and not guiones[i].isalpha():
                guiones[i] = y
                count +=1
                vueltas = 1
        if vueltas == 0:   
            vidas +=1   
                
        if count >= palabra_long: 
            print("\n -- > Cogratulation, you are win!!!")
            break
        elif vidas == 0:
            print("\n -- > Sorry, you lost !!!")
            break

        limpiar_pantalla()       
        interfase(guiones)
    print("Your word is --> " + str(palabra))

if __name__=="__main__":
    run()
