import json as js

with open('practise2.json','r') as a:
    data = js.load(a)

for dub in data["products"]:
    print(dub['item'],dub['quantity'])
    print(dub['item'],dub['price'])
    print(dub['quantity'],dub['price'])