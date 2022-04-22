from urllib import request
import json

def get_products(category):
    api_url = "https://api.escuelajs.co/api/v1/categories/%i/products/" % (category)

    reqres = request.urlopen(api_url)
    if (reqres.getcode()):  #We get a response code of 200 - Success
        jsonResponse = json.loads(reqres.read())
        total = print_products(jsonResponse)
        #print_products_by_category(total)
    else:
        print(f"Invalid status code {reqres.getcode()}")

def print_products(products):
    total = len(products)
    print(f"\nHay estos productos = {total}")
    for product in products:
        #print(product)
        id_ =  product["id"]
        title_ =  product["title"]
        price_ =  product["price"]
        description_ = product["description"]
        image_ =  product["images"][0]
        print(f"---\nid:[{id_}]\n\ttitle:{title_}\tprice:{price_}\n\tdescription:{description_}\n\timage:'{image_}'")


def get_products_by_category(total):
    if total > 0:
        category = int(input(f"***\nIntroduce el id de una categoria: entre 1 y {total}: "))
        if category > 0 and category <= total:
            get_products(category)
        else:
            print(f"\nERROR: El valor introducido está fuera de rango entre 1 y {total}")
    else:
        print("No hay categorias, cargue primero alguna categoria")


def print_categories(categories):
    total = len(categories)
    print(f"\nHay estas categorias = {total}")
    for category in categories:
        id_ =  category["id"]
        name_ =  category["name"]
        image_ =  category["image"]
        print(f"---\nid:[{id_}]\n\tname:{name_}\timage:'{image_}'")
    return total


def run():
    api_url = "https://api.escuelajs.co/api/v1/categories/"

    reqres = request.urlopen(api_url)
    if (reqres.getcode()):  #We get a response code of 200 - Success
        jsonResponse = json.loads(reqres.read())
        total = print_categories(jsonResponse)
        get_products_by_category(total)
    else:
        print(f"Invalid status code {reqres.getcode()}")

if __name__ == "__main__":
    run()