# Actividad número uno de técnicas de programación. 

# Resta 
def restar(PrimerNumero, SegundoNumero):
   return PrimerNumero + SegundoNumero

# Sumar 
def sumar(PrimerNumero, SegundoNumero):
    return PrimerNumero + SegundoNumero
    
# Dividir
def dividir(PrimerNumero, SegundoNumero):
    return PrimerNumero + SegundoNumero

# Multiplicar
def multiplicar(PrimerNumero, SegundoNumero):
    return PrimerNumero + SegundoNumero    

# Determina si es primo
def Primo(Numero):
    if Numero < 1:
        return 'Es primo'
    elif Numero == 2:
        return 'No es primo'
    else:
        for i in range(2,Numero):
            if Numero % i == 0:
             return 'No es primo'
            return 'Es primo'  

# Si numero es palíndromo
def esPalidromo(Numero): 
    Numero = str(Numero)
    if Numero == Numero[::-1]: 
        print("El número ingresado es palíndromo")
    else: 
        print("El número ingresado no es palíndromo")

#Menú de opciones
print("Calculadora iniciada, seleccione operacion a realizar: ")
print("1. Operación sumar")
print("2. Operación restar")
print("3. Operación multiplicar")
print("4. Operación dividir")
print("5. Operación verificar número primo")
print("6. Operación veficar número palíndromo")

while True:
    # Se ingresa la opción
    opcion = input("Indique la operación deseada: ")

    # Verificar las opciones
    if opcion in ('1', '2', '3', '4', '5', '6'):
       
        if opcion in ('1', '2', '3', '4'):
         numero1 = float(input("Ingrese el primer número: "))
         numero2 = float(input("Ingrese el segundo número: "))

         if opcion == '1':
            print(numero1, "+", numero2, "=", sumar(numero1, numero2))

         elif opcion == '2':
            print(numero1, "-", numero2, "=", restar(numero1, numero2))

         elif opcion == '3':
            print(numero1, "*", numero2, "=", multiplicar(numero1, numero2))

         elif opcion == '4':
            print(numero1, "/", numero2, "=", dividir(numero1, numero2))

        
        if opcion in ('5', '6'):
            numero = int(input("Ingrese el número que desea analizar: "))
            if opcion == '5':
                print(Primo(numero))

            elif opcion == '6':
                esPalidromo(numero)

        # Verificar si desea realizar otra operación
        Siguiente = input ("Desea continuar  (si/no): ")
        if Siguiente == "no" or Siguiente == "n":
            print("Operaciones finalizadas")
            break    

    else:
        print("La opción marcada no tiene validez.")
