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


if __name__ == "__main__":
    run()
