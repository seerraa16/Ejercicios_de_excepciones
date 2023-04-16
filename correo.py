# Permitir entrada a app si el correo es valido
import re
def correo_valido(correo):
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(patron, correo):
        return True
    else:
        return False
def main():
    correo = input("Correo: ")
    if correo_valido(correo):
        print("Este es su correo, tiene acceso a la app")
    else:
        print("No es valido, intetelo otra vez. recuerda que tiene que tener un formato asi: t@t.t ")
        return main()
        
def numero_intentos():
    intentos = 0
    while intentos < 3:
        main()
        intentos += 1
    print("Se ha excedido el numero de intentos")
print (numero_intentos())



