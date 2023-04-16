# Permitir entrada a app si el correo es valido
import re
def correo_valido(correo):
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(patron, correo):
        return True
    else:
        return False


