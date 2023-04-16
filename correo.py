def formato_correo(correo):
    if "@" in correo:
        return True
    else:
        return False
print("¿cual es su correo?")
correo = input()
