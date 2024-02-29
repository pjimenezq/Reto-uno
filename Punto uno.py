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

