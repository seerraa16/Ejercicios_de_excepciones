print("¿cual es su correo?")
correo = input()
def formato_correo(correo):
    if "@" "." in correo:
        return True
    else:
        return False
if formato_correo(correo):
    print("correo valido")
else:
    print("correo invalido")
    if not "@" in correo:
        print("falta el @")
    if not "." in correo:
        print("falta el .")
    print("correo invalido")

