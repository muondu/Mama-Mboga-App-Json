import json as js

with open('products.json','r') as s:
    products = js.load(s)
    print(type(products["itemName"]))
    for dub in products["itemName"]:
        print(dub)

