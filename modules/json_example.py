import json

# json module is used serialize and deserialize data while passing message in network calls

# serialization: converting python objects into json string
#python object(list, dict) --> str(json)

# deserialization: converting json to python objects


my_data = {
    'name': "Badra",
    'age': 29,
    'location': "Hyderabad"
}

json_data = json.dumps(my_data)


print(type(json_data))


# deserialization
my_object = json.loads(json_data)
print(type(my_object))




