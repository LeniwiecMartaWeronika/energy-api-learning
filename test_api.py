import requests # This is the "telephone" that calls the API

# We are calling a mock Energy API for practice
url = "https://jsonplaceholder.typicode.com" 

print("Marta, calling the Energy Data Server...")

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("--- DATA RECEIVED ---")
    print(f"Market Report Title: {data['title']}")
    print("----------------------")
    print("Success! You just made your first API call.")
else:
    print("Connection failed. Check your internet.")
