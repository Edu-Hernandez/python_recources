
"""FUNCIONES ANIDADAS"""

def operaciones():

    print("Escoge una opción: ")

    menu = "1. Multiplicar  2.Sumar  3.Restar  4.Dividir"

    print(menu)
    valor = int(input('ingrese el numero de operacion que desea realizar: '))
    
    numero1 = int(input("ingrese el primer numero: "))
    
    numero2 = int(input("ingrese el segundo numero: "))


    def restar():
        re = numero1 - numero2
        print("el resultado es: "+str(re))
    
    def sumar():
        su = numero2 + numero1
        print("el resultado es: "+str(su))
    
    def multiplicar():
        mul = numero1 * numero2
        print("el resultado es: "+str(mul))

    def Dividir():
        div = numero1 /numero2
        print("el resultado es: "+str(div))

    if valor == 1:
        multiplicar()
    if valor == 2:
        sumar()
    if valor == 3:
        restar()
    if valor == 4:
        Dividir()

print(operaciones())
    