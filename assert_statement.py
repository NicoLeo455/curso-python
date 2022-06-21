def divisors(num):
    dividor=[]                                    
    for i in range(1,num+1):      
        if num % i == 0:
            dividor.append(i)
    return dividor    


def run():   
    num = input("Digite un numero: ")
    assert num.isnumeric(), "Usted debe ingresar un numero"
    assert num<0, "No se aceptan numeros negativos"
    lista = divisors(int(num))
    print(lista)
    print("Termino el programa!!")


if __name__ == "__main__":
    run()