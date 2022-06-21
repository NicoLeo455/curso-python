from re import X

def run():

#    lista = []
#    for x in range(1,101):    
#        lista.append(x)

#cuadrado de los numeros que no sean divisibles por 3
#    lista2 =[]
#    for valor in lista:     
#        lista2 = valor**2
#        if lista2 % 3:
#            print(lista2)
    
#   Imprimir lista hasta el 100 raiz cuadrada de 2 de los numeros que no sean divisibles por 3
#   Usando list comprehensions

#    squares = [i**2 for i in range(1,101) if i % 3 != 0]
#    print(squares)

        #RETO DE LA CLASE
        squares = [i for i in range(1,1001) if i%4==0 and i%6==0 and i%9==0]
        for x in squares:  #Con esta linea se imprime en horizontal
            print(x) 
  
if __name__ == "__main__":
    run()



#     squares = [i for i in range(1,100) if i%4==0 and i%6==0 and i%9==0]
#     for x in squares: 
#       print(squares)     