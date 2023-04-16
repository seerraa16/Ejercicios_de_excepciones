# Permitir entrada a app si el correo es valido
def fromato_de_el_correo(correo):
    if (r"[^@]+@[^@]+\.[^@]+", correo):
        return True
    else:
        return False
print("Ingrese su correo")
correo = input()
if fromato_de_el_correo(correo):
    print("Su correo es valido")
else:
    print("Su correo no es valido")

