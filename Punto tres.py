#Función que recibe una lista de números enteros y devuelve solo aquellos que son primos

def primos(lista): #El argumento de la función corresponde a la lista de números enteros
    x : int = 2 #Se usa como divisor, para calcular el modulo entre el entero y x
    y : int = 0 #Se usa como la posición de la lista de enteros y permite acceder a cada uno de los números de la lista
    listaPrimos = [] #Posteriormente, se le añaden los números enteros que cumplen con las características de los primos
    
    while y<len(lista): #El ciclo se ejecuta hasta que se evaluen todos los números de la lista
        if x<=(lista[y]**0.5):
            if lista[y]%x==0: #Si el modulo es igual a 0, el número entero sí es primo
                y+=1 #Se suma una unidad, para evaluar si es primo el siguiente número de la lista
                x=2 #x vuelve a su valor original
            else:
                x+=1 #Se le suma una unidad a x y se repite el ciclo
        else:
            listaPrimos.append(lista[y]) #Se añade el número entero y primo a la lista de números primos
            y+=1 #Se suma una unidad, para evaluar si es primo el siguiente número de la lista
            x=2 #x vuelve a su valor original
    return listaPrimos

if __name__=="__main__":
    listaEnteros = []
    print("Este programa recibe una lista de números enteros y devuelve solo aquellos que son primos.") #Se imprime el objetivo del programa
    cantidadNumeros=int(input("Ingrese la cantidad de números enteros que hay en la lista "))
    for z in range(cantidadNumeros):
        entero=int(input("Digite el número entero que quiere ingresar a la lista "))
        if entero>1:
            listaEnteros.append(entero) #El usuario añade los enteros que desea a la lista de números enteros
    resultado = primos(listaEnteros) #Se llama la función creada anteriormente
    print("De la lista de números enteros: " + str(listaEnteros) +", los números que son primos son: " + str(resultado))