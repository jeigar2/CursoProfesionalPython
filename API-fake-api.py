from urllib import request
import json

api_url = "https://api.escuelajs.co/api/v1/categories/"

reqres = request.urlopen(api_url)
if (reqres.getcode()):  #We get a response code of 200 - Success
    jsonResponse = json.loads(reqres.read())
    print(f"\nJson Response is =   {jsonResponse}")
    for category in jsonResponse:
        id_ =  category["id"]
        name_ =  category["name"]
        image_ =  category["image"]
        print(f"\nlinea{id_}\n\tname:{name_}\timage:'{image_}'")
else:
    print (f"Invalid status code {reqres.getcode()}")
    