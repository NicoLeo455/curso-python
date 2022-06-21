# Crear [1,4,5,6,9,13,19,21] de la lista de abajo
# [1,5,9,13,19,21]


def run():
    lista = [1,2,3,4,5]

    #lista_impares = {i**2 for i in lista}  
    lista_impares = list(map(lambda x : x**2,lista))

    print(lista_impares)




if __name__ == "__main__":
    run()