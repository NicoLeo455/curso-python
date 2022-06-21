def run():
    
    #lista para filter
    lista = [1,4,5,6,9,13,19,21]

    #lista para map
    #lista = [1,2,3,4,5]

    #lista para reduce
    #lista = [2,2,2,2,2]


    #Funcion filter
    #lista_impares = {i for i in lista if i%2!=0}
    #lista_impares = list(filter(lambda x:x%2!=0,lista))

    #print(lista_impares) 

    #Funcion Map
    #squares = {i**2 for i in lista}  
    #squares = list(map(lambda x : x**2,lista))
    #print(squares) 

    #Funcion Reduce

    #all_multiplate=1
    #for i in lista:
    #    all_multiplate=all_multiplate*i
    #print(all_multiplate)

         
if __name__ == "__main__":
    run()


#Lambda function

#resaltar_valor= lambda valor: "¡{}! $".format(valor)
#comision_ana=154564
#print(resaltar_valor(comision_ana))

#Ejemplo con Filter
'''
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):      #Imprime el mensaje en automatico
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)    

ListaEmpleados= [
        Empleado("Julian","Director",150000),
        Empleado("Maria","Secretaria",85000),
        Empleado("Nazareno","Contador",95000),
        Empleado("Nicolas","Administrador",75000),
        Empleado("Juan","Limpieza",55000), 
]

#ListaEmpleados filtra segun si sale true o false del filter y se va guardando en salarios_altos
Salarios_altos=filter(lambda Empleado: Empleado.salario>80000, ListaEmpleados)

for i in Salarios_altos:
    print(i)
'''
'''
#Ejemplo con Map
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):      #Imprime el mensaje en automatico
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)    

ListaEmpleados= [
        Empleado("Julian","Director",150000),
        Empleado("Maria","Secretaria",85000),
        Empleado("Nazareno","Contador",95000),
        Empleado("Nicolas","Administrador",75000),
        Empleado("Juan","Limpieza",55000), 
]

ListaEmpleadosComision= map(lambda Empleado: Empleado.salario * 1.03,ListaEmpleados)

for i in ListaEmpleadosComision:
    print(i)
'''
