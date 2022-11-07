def divisors(num):
    dividor=[]
    try:
        if num <0:
              raise ValueError("No se pueden ingresar numeros negativos")
        else:                             #List comprehension, se guarda todo como lista  
            for i in range(1,num+1):      #divisors = [i for i in range(1, num + 1) if num % i == 0] return divisors
                if num % i == 0:
                  dividor.append(i)
            return dividor    
    except ValueError as ve:
        print(ve)
    return str(num)+ " no es un numero positivo"         


def run():  
    try:
        
        num = int(input("Digite un numero: "))
        lista = divisors(num)
        print(lista)
        print("Termino el programa!!")
        
    except:
        print("No se deben ingresar letras")

if __name__ == "__main__":
    run()