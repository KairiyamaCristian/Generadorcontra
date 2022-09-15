import random

#function que devuelve un string_random a partir de una lista
def limitar_random(num,lista_caracter):
    list_random = []
    for i in range(num):
        caracter_random = random.choice(lista_caracter)
        list_random.append(caracter_random)
    return list_random



def generar_contrasena():

    #Separamos los components
    lista_mayuscula= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lista_minuscula= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_numeros= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lista_simbolos= ['!', '&', '$', '(', ')', '?']

    #creamos void list
    mayusculas = []
    minusculas = []
    numeros = []
    simbolos = []
    palabras = []

    #restringimos cantidad
    mayusculas = limitar_random(5,lista_mayuscula)
    minusculas = limitar_random(0,lista_minuscula)
    numeros = limitar_random(5,lista_numeros)
    simbolos = limitar_random(6,lista_simbolos)

    palab = input('Introduce la palabra que quieras agregar: ')

    #introducir nuevas palabras con la contrasena
    while( palab!= '0' ):
        palabras.append(palab)
        palab = input('Introduce otra palabra que quieras agregar: ')

    #metemos en una misma lista (mutabilidad)
    caracteres = simbolos + numeros + mayusculas + minusculas + palabras

    contrasena = limitar_random(5,caracteres)
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('tu nueva contrasena es: '+ contrasena)


if __name__=='__main__':
    run()