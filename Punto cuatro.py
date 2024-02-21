# Función que recibe una lista de números enteros y retorna la mayor suma entre dos elementos consecutivos

def sumamayor(lista):
    listaSumatorias=[]
    x:int=0
    y:int=1
    while y<len(lista):
        listaSumatorias.append(lista[x]+lista[y])
        x+=1
        y+=1
    return max(listaSumatorias)

if __name__=="__main__":
    listaEnteros=[]
    print("Este programa recibe una lista de números enteros y devuelve la mayor suma entre dos elementos consecutivos.")
    cantidadNumeros=int(input("Ingrese la cantidad de números enteros que hay en la lista "))
    for z in range(cantidadNumeros):
        entero=int(input("Digite el número entero que quiere ingresar a la lista "))
        listaEnteros.append(entero)
    resultado=sumamayor(listaEnteros)
    print("De la lista de números enteros, la mayor suma entre dos elementos consecutivos es " + str(resultado))
