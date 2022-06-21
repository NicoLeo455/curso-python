from multiprocessing.sharedctypes import Value
from optparse import Values
from math import sqrt


def run():

#    dictionary = {}
#    for i in range(1,101):
#        if i%3 != 0:
#            dictionary[i] = i**3

#    for keys,Values in dictionary.items():
#        print("Natural_numbers ",keys,": Cubed_numbers ", Values)

    my_dicts = {i:i**3 for i in range(1,101) if i % 3 !=0}  #Omitir los numeros divisibles por 3
    print(my_dicts)

    #Reto: crear dictionaty comprehension cuyas llaves sean los 1000 primeros numeros naturales 
    # con sus raices cuadradas como valores

#    my_dictionary = {i:sqrt(i) for i in range (1,101)}
#    print(my_dictionary)


if __name__ == "__main__":
    run()