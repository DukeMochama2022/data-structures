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

def  place_order(index, quantity):
    data=load_data()
    if not data['products']:
        print("No products available.")
        return

    if index < 1 or index  > len(data['products']):
        print("Invalid product index.")
        return

    product=data["products"][index-1]

    if product ["stock"] <quantity:
        print("Insufficent stock.")
        return
    product["stock"]-=quantity
    order={"product":product["name"], "quantity":quantity,"price":product["price"], "total":product["price"]*quantity}
    data['orders'].append(order)
    save_data(data)
    print(f"Order for {quantity} {product['name']} placed successfuly.")  

def view_orders():
    data=load_data()
    if not data["orders"]:
        print("No orders placed yet.")
        return
    print("Order history.") 
    for i, order in enumerate(data['orders']):
        print(f"{i + 1}. {order['quantity']} {order['product']} - Total: ${order['total']}") 

if __name__ =="__main__":
    while True:
        print("\nE-commerce System")
        print("1. Add product")
        print("2. View product")
        print("3. Order product")
        print("4. View orders")
        print("5. Quit")

        choice=int(input("Enter your choice:"))

        if choice == 1:
            name=input("Enter product name...")
            price=float(input("Enter product price..."))
            stock=int(input("Enter initial stock..."))
            add_product(name,price,stock)








