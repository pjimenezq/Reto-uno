#Función que permite validar si una palabra es un palíndromo

def palindromo(palabra:str):
    x: int = 0
    y: int = -1
    palindromo:bool = True
    while x<len(palabra) and palindromo==True:
        if palabra[x]==palabra[y]:
            x+=1
            y-=1
        else:
            palindromo = False
            return("La palabra '" + palabra +"' no es un palíndromo.")
    
    if palindromo==True:
        return("La palabra '" + palabra +"' sí es un palíndromo.")

if __name__=="__main__":
      print("Este programa permite validar si una palabra ingresada por el usuario es un palíndromo.")
      a = str(input("Ingrese la palabra que desee (asegúrese de escribirla toda en mayúsculas o toda en minúsculas) "))
      resultado = palindromo(a)
      print(resultado)