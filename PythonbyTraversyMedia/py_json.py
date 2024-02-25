# JSON is commonly used with data APIS. Here how we can parse json into a python dictionary.


import json

# sample json 

userJSON = '{"first_name": "john", "last_name": "Doe", "age": 30}'

# Parse the dictionary 
# Parse (deserialize) the JSON string back into a Python dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])


# Parse (deserialize) the JSON string back into a Python dictionary

car = {'make': 'ford', 'model': 'Mustang', 'year': 1989}

carJSON = json.dumps(car)

print(carJSON)