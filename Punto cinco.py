# Función que recibe una lista de string y retorna aquellos elementos que tengan los mismos caracteres.

def anagrama(lista):
    listaDos=[] #Luego, se le añade a esta lista los elementos que tienen los mismo caracteres
    x=0 #Se utiliza para acceder al primer string de la lista
    y=0 #Se utiliza para acceder a cada una de las letras del primer string
    z=0 #Se utiliza para acceder a cada una de las palabras de las lista

    while z<len(lista):
        bandera=True
        while y<len(lista[x]):
            if lista[x][y] in lista[z]:#Cuando la letra con la posición y del primer string se encuentra en la palabra con la posición z, se evalua la siguiente letra
                y+=1
            else:
                bandera=False
                z+=1#Se suma una unidad para evaluar la siguiente palabra
                y=0
        if bandera==True:
            listaDos.append(lista[z])#Se añade la palabra con los mismo caracteres a la segunda lista
            y=0
            z+=1

    return listaDos

if __name__=="__main__":
    lista=[]
    print("Este programa recibe una lista de strings y retorna aquellos elementos que tengan los mismos caracteres.") #Se imprime el objetivo del programa
    cantidadPalabras=int(input("Ingrese la cantidad de cadenas que hay en la lista "))
    for z in range(cantidadPalabras):
        cadena=str(input("Digite la cadena que quiere ingresar a la lista "))
        lista.append(cadena)  #El usuario añade las cadenas que desea a la lista de strings
    resultado=anagrama(lista) #Se llama la función creada anteriormente
    print("De la lista de strings, aquellos elementos que tienen los mismos caracteres son " + str(resultado))