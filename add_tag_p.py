def add_tag_p(func):
    def wrapper(string):
        print ("<p>" + string + "</p>")
    return wrapper


@add_tag_p
def parrafo(str):
    return str

def run():
    parrafo("Cum laudem")


if __name__ == "__main__":
    run()
