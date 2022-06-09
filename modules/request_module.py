import requests

# dummy_url https://jsonplaceholder.typicode.com/
# GET --> getting data from server
# POST --> sending data from client to server
# PUT --> update existing records
# Delete --> delete the resource in server

url = 'https://jsonplaceholder.typicode.com/posts/2'

response = requests.get(url)
print(response.status_code)
print(response.json())

import pprint
url2 ='https://jsonplaceholder.typicode.com/posts'
res2 = requests.get(url2)
pprint.pp(res2.json())







#downlaod image to your computer
image_url = "https://i.pinimg.com/originals/9c/b0/70/9cb070d62dc738a0c3a1a408d68e4af5.jpg"

response = requests.get(image_url)

file_buffer = response.content
print(file_buffer)

with open("myimage.jpeg", 'wb') as obj:
    obj.write(file_buffer)



