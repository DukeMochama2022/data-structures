import json

DATA_FILE='ecommerce_data.json'

#load data from the json file.
def load_data():
    try:
        with open (DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"products":[],"orders":[]}

#save data and information to the json file.
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data,f,indent=4)

#add product
def add_product(name, price, stock):
    data=load_data()
    product={"name":name, "price":price, "stock":stock}
    data["products"].append(product)
    save_data(data)
    print(f"Product {name} added successifully.")

#view products in the cart
def view_products():
    data=load_data()
    if not data["products"]:
        print("No prodcuts available.")
        return
    print("Available products.")
    for i, product in enumerate(data["products"]):
        print(f"{i + 1}. {product['name']} - ${product['price']} (Stock: {product['stock']})")




