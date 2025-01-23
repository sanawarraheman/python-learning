book ={}

book['tom'] = {
    "name": 'tom',
    'address': 'xyz',
    'phone': 145887489
}

book['bob'] = {
    "name": 'bob',
    'address': 'abc',
    'phone': 457956966
}
f=open('c://data/json.txt', 'r')
s=f.read()
print(s)
import json
json.loads(s)