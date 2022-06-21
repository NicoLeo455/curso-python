import platform
import os
import time
'''
#La función enumerate()
lista = ["Agustin","Rodrigo","Martin","Emilio","javier"]

#list(enumerate(lista))

for i,y in enumerate(lista,1):
    print(i,":",y)
'''



'''
#Metodo Get
mi_agenda={
    "Nicolas": 54656,
    "Facundo":1234,
    "Rocio":4567,
    "Emilio":7894,
    "Juan":4321,
    "Matias":5555,
} 

#print(mi_agenda.get("Nicolas")) #Me imprime el codigo guardado en ese

#En el caso de que no este en el diccionario

x = input("Ingrese un nombre: ")
print(mi_agenda.get(x))
#Si no existe el indice nombre dispara un NONE o un mensaje (opcional)
'''


def limpiar_pantalla():
    time.sleep(2)

    if platform.system() == 'Windows':
        os.system ("cls")

def run():

    mi_agenda={
    "Nicolas": 54656,
    "Facundo":1234,
    "Rocio":4567,
    "Emilio":7894,
    "Juan":4321,
    "Matias":5555,
    }      

    x = input("Ingrese un nombre: ")
    print(mi_agenda.get(x))

    limpiar_pantalla()


if __name__=="__main__":
    run()
