# Reto uno

**Instrucción**

Para cada punto cree un programa individual. El repositorio debe tener una corta explicación de cómo llegó a la solución.

## Punto uno
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación.

**Código**
```
# Función que realiza operaciones básicas entre dos números

def operaciones(x:float, y:float, operacion:str)->float: #Los argumentos de la función corresponden respectivamente al primer número, el segundo número y el símbolo de la operación
    if operacion == "+":
        return x+y
    elif operacion == "-":
        return x-y
    elif operacion == "*":
            return x*y
    elif operacion == "/":
            if y != 0: #Solo se hace la operación si el segundo número es distinto a 0
                return x/y
            else:
                return "No se puede dividir entre 0"
    else:
          return "El caracter que corresponde a la operación no es válido."
    
if __name__=="__main__":
      print("Este programa realiza operaciones básicas (suma, resta, multiplicación y división) entre dos números.")#Se imprime el objetivo del programa
      a = float(input("Ingrese el primer operando "))
      b = float(input("Ingrese el segundo operando "))
      operador = str(input("Ingrese el caracter que corresponde a la operación que desea realizar "))
      resultado = operaciones(a, b, operador) #Se llama la función creada
      print(resultado)
```

**Explicación**

En el primer punto, se crea una función llamada _operaciones_. Esta función tiene como argumentos _x_ (que es de tipo flotante y corresponde al primer número de la operación), _y_ (que es de tipo flotante y corresponde al segundo número de la operación) y _operacion_ (que es de tipo string y corresponde al símbolo de la operación).

Dentro de la función, se encuentra una estructura _if-elif-else_. Esta permite que se ejecute la operación de suma, resta, multiplicación o división entre los dos números dependiendo del carácter ingresado para la operación. Cuando el carácter ingresado no corresponde a ninguna de las operaciones se imprime el mensaje _“El carácter que corresponde a la operación no es válido.”_ En el caso de la división se usa la estructura _if-else_, donde la operación se lleva a cabo solo si el segundo número es distinto a 0.

Posteriormente, se usa la función _main_, donde se imprime la funcionalidad del programa y se declaran e inicializan con la función _input_ las variables correspondientes al primer número, el segundo número y el operador. Por último, se llama la función creada anteriormente y se imprime el resultado.

## Punto dos
Realice una función que permita validar si una palabra es un palíndromo. 

**Código**
```
#Función que permite validar si una palabra es un palíndromo

def palindromo(palabra:str): #El argumento de la función corresponde a la palabra que se quiere validar como palíndromo
    x: int = 0 #Se usa para obtener la primera letra de la palabra
    y: int = -1 #Se usa para obtener la última letra de la palabra
    palindromo:bool = True
    while x<len(palabra) and palindromo==True:
        if palabra[x]==palabra[y]:
            x+=1 #Se aumenta el valor, para obtener la siguiente letra
            y-=1 #Se disminuye el valor, para obtener la letra anterior
        else:
            palindromo = False #Cuando las letras no son iguales, la palabra no es palíndromo
            return("La palabra '" + palabra +"' no es un palíndromo.")
    
    if palindromo==True: #Cuando se acaba el ciclo while y siempre coincidieron las letras, la palabra es palíndromo
        return("La palabra '" + palabra +"' sí es un palíndromo.")

if __name__=="__main__":
      print("Este programa permite validar si una palabra ingresada por el usuario es un palíndromo.") #Se imprime el objetivo del programa
      a = str(input("Ingrese la palabra que desee (asegúrese de escribirla toda en mayúsculas o toda en minúsculas) "))
      resultado = palindromo(a) # Se llama la función creada anteriormente
      print(resultado)
```

**Explicación**

Para el segundo punto, se crea una función llamada _palindromo_. Esta función tiene como argumento _palabra_ (que es de tipo string y corresponde a aquella palabra que se quiere validar como palíndromo).

Dentro de la función, se declaran las variables _x_ y _y_, las cuales se inicializan con los valores 0 y -1 respectivamente. Asimismo, se declara la variable de tipo booleana _palindromo_, la cual se inicializa con el valor _True_.

Se usa un ciclo _while_, que empieza comparando la primera letra de la palabra con la última letra de esta misma. En el caso de que estas sean iguales, se suma una unidad a _x_ y se le resta una unidad a _y_, lo que implica que ahora se va a comparar la segunda letra de la palabra con la penúltima letra. Este ciclo se seguirá ejecutando mientras la palabra siga cumpliendo la condición de palíndromo y mientras no se hayan comparado todas las letras de la palabra. 

Cuando las letras no coincidan, el booleao _palindromo_ cambiará a valor _False_ y la función retornará la frase _”La palabra no es un palíndromo”_. Asimismo, si ya se evaluó y confirmó la coincidencia de todas las letras de la palabra, el booleano mantendrá el valor _True_, se acabará el ciclo _while_ y se retornará la frase _”La palabra sí es un palíndromo.”

Posteriormente, se usa la función _main_, donde se imprime la funcionalidad del programa y se declara e inicializa con la función _input_ la variable correspondiente a la palabra. Por último, se llama la función creada anteriormente y se imprime el resultado.

## Punto tres
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos.

**Código**
```
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
```
**Explicación**

Para el tercer punto, se crea una función llamada _primos_. Esta función tiene como argumento una lista, que corresponde a la lista de números enteros. En primer lugar, dentro de la función, se declaran las variables _x_ y _y_, las cuales se inicializan con los valores 2 y 0 respectivamente. Asimismo, se declara la variable _listaPrimos_, que corresponde a una lista vacía.  La variable _x_ funciona como el divisor, cuando el modulo entre el número de la lista y x, es igual a 0, el número no es primo. La variable _y_ corresponde a la posición de la lista, esta variable permite acceder a cada uno de los números que se encuentran dentro de la lista.  

En el código, se usa un ciclo _while_, que se ejecutará hasta que se hayan evaluado todos y cada uno de los números enteros que se encuentran en la lista de entrada. En el ciclo se usa una estructura _if-else_, en la cual, si la raíz del número entero de la lista es menor al divisor, se añade ese número entero a la lista de los números primos, usando _append_ y se procede a evaluar si el siguiente número de la lista es primo. En caso contrario, se procede a hallar el modulo entre ese número entero y el divisor, si el resultado es igual a 0, el número no es primo y se procede a evaluar si el siguiente número de la lista es primo. Sin embargo, si el resultado del modulo no es igual a 0, se le suma una unidad al divisor y se repite el ciclo.

_Si quiere saber la razón por la que se afirma que cuando la raíz del número entero de la lista es menor al divisor el número es primo, observe el siguiente video: https://www.youtube.com/watch?v=9iH8mY3iGLk_

Cuando se acaba el ciclo, la función retorna la lista de los primos. A continuación, se usa la función _main_, donde se imprime la funcionalidad del programa y se crea la lista vacía _listaEnteros_. Luego, se le pide al usuario que ingrese la cantidad de números enteros que tiene la lista, para que esa sea la cantidad de veces que el usuario pueda ingresar un entero, que se añade a _listaEnteros_ utilizando _append_. Para finalizar, se llama la función creada anteriormente y se imprime el resultado.

## Punto cuatro
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

**Código**

**Explicación**

## Punto cinco
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. 
**Código**

**Explicación**

