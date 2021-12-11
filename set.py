def mi_funcion():
    colores_semaforo = {"rojo", "amarillo", "verde"}
    colores_empieza_a = {"amarillo", "azul", "añil", "ambar"}
    print(colores_semaforo)
    print(colores_empieza_a)
    print(colores_empieza_a | colores_semaforo)
    print(colores_empieza_a & colores_semaforo)
    print(colores_empieza_a - colores_semaforo)
    print(colores_semaforo - colores_empieza_a)
    print(colores_semaforo ^ colores_empieza_a)

def remove_duplicates(some_list):
    my_set = set(some_list)
    new_List = []
    for element in my_set:
        new_List.append(element)
    return new_List


def run():
    my_list = [1,1,2,2,4]
    print(my_list)
    print(remove_duplicates(my_list))
    #mi_funcion()


if __name__ == "__main__":
    run()
