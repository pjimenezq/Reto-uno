#Función que recibe una lista de números enteros y devuelve solo aquellos que son primos

def primos(lista):
    x:int=2
    y:int=0
    listaprimos=[]
    
    while y<len(lista):
        if x<=(lista[y]**0.5):
            if lista[y]%x==0:
                y+=1
                x=2
            else:
                x+=1
        else:
            listaprimos.append(lista[y])
            y+=1
            x=2
    return listaprimos

if __name__=="__main__":
    listaEnteros=[]
    print("Este programa recibe una lista de números enteros y devuelve solo aquellos que son primos.")
    cantidadNumeros=int(input("Ingrese la cantidad de números enteros que hay en la lista "))
    for z in range(cantidadNumeros):
        entero=int(input("Digite el número entero que quiere ingresar a la lista "))
        if entero>1:
            listaEnteros.append(entero)
    resultado = primos(listaEnteros)
    print("De la lista de números enteros: " + str(listaEnteros) +", los números que son primos son: " + str(resultado))