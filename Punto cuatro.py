# Función que recibe una lista de números enteros y retorna la mayor suma entre dos elementos consecutivos

def sumaMayor(lista): #El argumento de la función corresponde a la lista de números enteros
    listaSumatorias = [] #Luego, se le añaden todas las sumatorias entre los elementos consecutivos
    x : int = 0 #Se usa para acceder a los números de la lista, según su posición
    y : int = 1 #Se usa para acceder al número consecutivo de x en la lista 

    while y<len(lista):
        listaSumatorias.append(lista[x]+lista[y]) #Se le agrega a la lista la suma entre los números consecutivos
        x+=1
        y+=1
    return max(listaSumatorias) #La función retorna la suma con el valor mayor

if __name__=="__main__":
    listaEnteros=[]
    print("Este programa recibe una lista de números enteros y devuelve la mayor suma entre dos elementos consecutivos.") #Se imprime el objetivo del programa
    cantidadNumeros=int(input("Ingrese la cantidad de números enteros que hay en la lista "))
    for z in range(cantidadNumeros):
        entero=int(input("Digite el número entero que quiere ingresar a la lista "))
        listaEnteros.append(entero)  #El usuario añade los enteros que desea a la lista de números enteros
    resultado=sumaMayor(listaEnteros) #Se llama la función creada anteriormente
    print("De la lista de números enteros, la mayor suma entre dos elementos consecutivos es " + str(resultado))
