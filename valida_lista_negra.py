import random

diccionario = {
    "dinero":["dinero", "euro", "moneda", "billete"],
    "juguete":["juguete", "balon", "muñeca", "tren"],
    "número":["número", "uno", "cien", "par"],
    "ojo":["ojo", "vista", "ver", "pupila"],
    "hermano":["hermano","padre","hijo","primo"],
    "mermelada":["mermelada", "confitura","azucar","fresa"]
}

def valida_lista_negra(func):
    def wrapper(*args, **kwargs):
        palabras_prohibidas = diccionario.get(args[0])
        for palabra in palabras_prohibidas:
            if args[1].lower() == palabra:
                print ("**Alerta: ha utilizado una palabra tabú** ")
                return
        print ("Palabra validada: OK")
        func(*args, **kwargs)
    return wrapper


@valida_lista_negra
def introducir_palabra(key, value):
    print(value)


def run():
    intentos = 3
    key = random.choice(list(diccionario.keys()))
    while(intentos > 0):
        palabra = input("## Escriba una palabra para definir "+ key + ", recuerda que hay palabras tabu. Le quedan " + str(intentos) + " intentos: ")
        introducir_palabra(key, palabra)
        intentos-= 1


if __name__ == "__main__":
    run()
