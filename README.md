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

**Explicación**

## Punto tres
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos.
**Código**

**Explicación**

## Punto cuatro
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

**Código**

**Explicación**

## Punto cinco
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. 
**Código**

**Explicación**

