# Función que realiza operaciones básicas entre dos números

def operaciones(x:float, y:float, operacion:str)->float:  
    if operacion == "+":
        return x+y
    elif operacion == "-":
        return x-y
    elif operacion == "*":
            return x*y
    elif operacion == "/":
            return x/y
    else:
          return "El caracter que corresponde a la operación no es válido."
    
if __name__=="__main__":
      print("Este programa realiza operaciones básicas (suma, resta, multiplicación y división) entre dos números.")
      a = float(input("Ingrese el primer operando "))
      b = float(input("Ingrese el segundo operando "))
      operador = str(input("Ingrese el caracter que corresponde a la operación que desea realizar "))
      resultado = operaciones(a, b, operador)
      print(resultado)
