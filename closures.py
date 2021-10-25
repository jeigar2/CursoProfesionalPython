def make_repeat_of(numero):
    def repeater(string):
        assert type(string) == str, "Debe introducir una cadena"
        return string * numero
    return repeater


def run():
    repetir3veces = make_repeat_of(3)
    print (repetir3veces("¡Dios te Ama!"))
    repetir5veces = make_repeat_of(5)
    print (repetir5veces("¡Alaba a Dios!"))


if __name__ == "__main__":
    run()
