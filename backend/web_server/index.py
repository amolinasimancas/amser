import store

def run():
    categories = store.get_categories()
    products = store.get_products()
    users = store.get_users()
    
    print(f"Categories: {categories}")
    print(f"Products: {products}")
    print(f"Users: {users}")