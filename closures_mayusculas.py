def mayusculas(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

def run():
    print (mensaje("Ignacio"))


if __name__ == "__main__":
    run()

