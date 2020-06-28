# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample JSON
userJSON = '{"firstName": "John", "lastName": "Doe", "age": 30}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['firstName'])

# parse to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)