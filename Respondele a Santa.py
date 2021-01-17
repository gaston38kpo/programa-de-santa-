# Funcion de la respuesta de Santa.
def santaResponde(x, y):
    santaRespondeSuma = x + y
    return santaRespondeSuma


# Aca Santa hace una pregunta y espera la respuesta si/no de los niños.
try:
    n1RespondenASanta = input("Como te llamas?: ")
    n2RespondenASanta = input(f"Ya es navidad {n1RespondenASanta}?: ")
except:
    print("Ocurrió un error")
    raise

# Funcion que evalúa que responder acorde a lo ingresado.


def esNavidad():

    if n2RespondenASanta.lower() == "si":
        return santaResponde(f"⛄ Rega", "los {n1RespondenASanta}!!🎅🎁🎄🎁")

    elif n2RespondenASanta.lower() == "no":
        return santaResponde(f"🙏🎅 Paciencia {n1RespondenASanta}, ya ", "iré en navidad, solo espera un poco mas ٩( ° ᴗ ° )۶ ")

    else:
        return "Solo te puedo responder si/no. (ง ͡> ͜ʖ ͡<)ง"


# Respuesta de santa.
respuesta = esNavidad()

print(respuesta)

# Fin programa
