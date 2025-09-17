import requests

def get_categories():
    response = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(response.status_code)
    return response.json()

def get_products():
    response = requests.get("https://api.escuelajs.co/api/v1/products")
    print(response.status_code)
    return response.json()

def get_users():
    response = requests.get("https://api.escuelajs.co/api/v1/users")
    print(response.status_code)
    return response.json()