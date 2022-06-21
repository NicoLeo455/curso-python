def run():
    my_list = [1,"Hello",True,4.5]
    my_dicts = {"firstname": "Facundo", "Lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "Lastname": "Garcia"},
        {"firstname": "Nico", "Lastname": "Gomez"},
        {"firstname": "Sair", "Lastname": "Sosa"},
        {"firstname": "Pablo", "Lastname": "Torres"},
        {"firstname": "Andres", "Lastname": "Alvarez"},
            ]   
            
    super_dicts= {
        "natural_numbs":[1,2,3,4,5],
        "integer_numbs":[-1,-2,0,2,1],
        "floating_numbs":[1.3, 2.85, 6.34]
       }

    #Imprimir una hecho con listas en su interior
    for i,y in super_dicts.items():
      print(i,"--",y)

    print("\n")
    
    #Imprimir una lista con diccionarios en su interior
    for i in super_list:
        for keys,values in i.items():
            print(keys,":",values)


if __name__ == "__main__":
    run()


