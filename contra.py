import random

def generar_contrasena():

    #Separamos las partes que incorporara la contraseña
    palabras = ['case', 'small', 'not', 'yesterday', 'now']
    palabrasespanol = ['casa', 'rata', 'mamifero', 'perro']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos =['!', '-', "$", "&"]

    #metemos en una misma lista (mutabilidad)
    caracteres= simbolos + numeros

    #creamos una lista vacia "contraseña"
    contrasena= []

    #Ponemos "5" caracteres random
    for i in range(5):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('tu nueva contrasena es: '+ contrasena)


if __name__=='__main__':
    run()