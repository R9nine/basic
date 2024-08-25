"""
#
# Part: Python JSON
# API = Application Progarmming Interface
#
"""
import json

# make a json(String)
x = '{"name", "John", "age": 20, "city": "Phuket"}'
print(x)

# parse
y = json.load(x)

# python dictinary
print(y)
print(type(y))
print(y["city"])

# python dictinary
a = {
    "name": "Noa",
    "age": 20,
    "city": "Phuket"
}
# convert to JSON (String)
b = json.dumps(a)

# JSON String
print(b)

