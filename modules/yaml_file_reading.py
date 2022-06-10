# pip install pyyaml

import yaml
from yaml.loader import SafeLoader


file_name = "verify_apache.yaml"
#
# with open(file_name, 'r') as file_obj:
#     data = yaml.load(file_obj, Loader=SafeLoader)
#     print(len(data))


# we should use load all when yaml contains multiple doccuments

with open(file_name, 'r') as file_obj:
    data = yaml.load_all(file_obj, Loader=SafeLoader)
    print(list(data))


# load is used to load the yaml that contains single document
# load_all is used to load the yaml that contains multiple documents


# how to write the data to yaml file

college_details = {
    "college_name": "CBIT",
    "address": "Hyderabad",
    "branches": ["hyderabad", "Bangalore", "Pune"]
}
"""
- college_name: "CBIT"
- address: "hyderabad"
- branches:
  - Hyderabad
  - HDHDH
  - KKK
"""

file_name = "college_details.yaml"
with open(file_name, 'w') as file_obj:
    yaml.dump(college_details, file_obj)



# Lets read this file
with open(file_name, 'r') as obj:
    data = yaml.load(obj,Loader=SafeLoader)
    print(data)


companies = [
    {
        "name": "wipro",
        "branches": ['hyderabad', "pune", "bangalore"]
    },
    {
        'name': "infosys",
        "branches": ['hyderabad']
    },
    {
        'name': "tcs",
        "branches": ['hyderabad', "Bangalore"]
    }
]

file_name = "companies.yaml"
with open(file_name, 'w') as obj:
    yaml.dump(companies, obj)


with open(file_name, 'r') as obj:
    data = yaml.load(obj, Loader=SafeLoader)
    print(data)