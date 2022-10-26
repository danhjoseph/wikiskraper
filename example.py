import requests

# Make a request to the API
query = "TaylorSwift"
response = requests.get("http://127.0.0.1:8000/wiki/" + query + "/summary")
print(response.json())
