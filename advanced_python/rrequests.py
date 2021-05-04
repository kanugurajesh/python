import requests
data = {
    "shiva":"the auspicious one",
    "mahadev":"the lord of all gods"
}
# who are gods

r1 = requests.post("https://www.geeksforgeeks.org/post-method-python-requests/",data)
print(r1.text)
print(r1.json)