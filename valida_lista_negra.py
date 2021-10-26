palabras_prohibidas = ["euro", "dinero", "moneda", "billete"]

def valida_lista_negra(func):
    def wrapper(*args, **kwargs):
        for palabra in palabras_prohibidas:
            if args[0].lower() == palabra:
                print ("**Alerta: ha utilizado una palabra tabú** ")
                return
        print ("Palabra validada: OK")
        func(*args, **kwargs)
    return wrapper

@valida_lista_negra
def introducir_palabra(string):
    print(string)

def run():
    intentos = 3
    while(intentos > 0):
        palabra = input("## Escriba una palabra para definir dinero, recuerda que hay palabras tabu. Le quedan " + str(intentos) + " intentos: ")
        introducir_palabra(palabra)
        intentos-= 1


if __name__ == "__main__":
    run()
