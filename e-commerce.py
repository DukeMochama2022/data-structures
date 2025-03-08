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

def delete_product(index):
    data=load_data()
    if not  data['products']:
        print("No prodcuts available.")
        return

    if index < 1 or index > len(data['products']):
        print("Invalid index.")
        return
    deleted_product=data["products"].pop(index -1)
    save_data(data)
    print(f"Product '{deleted_product['name']}' deleted successfully.")       

def delete_order(index):
    data=load_data()
    if not data['orders']:
        print("No available orders.")
        return

    if index < 1 or index > len(data['orders']):
        print("Invalid index")
        return
    deleted_order=data['orders'].pop(index-1)
    save_data(data)
    print(f"Order for {deleted_order['quantity']} {deleted_order['product']} deleted successfully.")      
    
if __name__ =="__main__":
    while True:
        print("\nE-commerce System")
        print("1. Add product")
        print("2. View product")
        print("3. Order product")
        print("4. View orders")
        print("5. Delete product")
        print("6. Delete order")
        print("7. Quit")

        choice=int(input("Enter your choice:"))

        if choice == 1:
            name=input("Enter product name...")
            price=float(input("Enter product price..."))
            stock=int(input("Enter initial stock..."))
            add_product(name,price,stock)

        elif choice ==2:
            view_products()

        elif choice ==3:
            view_products()
            if load_data()['products']:
                try:
                    index=int(input("Enter product number :"))
                    quantity=int(input("Enter product quantity :"))
                    place_order(index,quantity)
                except ValueError:
                    print("Invalid input. Enter numbers.")    

        elif choice == 4:
            view_orders()

        elif choice ==5:
            view_products()
            if load_data()["products"]:
                try:
                    product_index = int(input("Enter product number to delete: "))
                    delete_product(product_index)
                except ValueError:
                    print("Invalid input. Please enter numbers.")

        elif choice == 6:
            view_orders()
            if load_data()['orders']:
                try:
                    index = int(input("Enter order number to delete."))
                    delete_order(index)
                except ValueError:
                    print("Error occured please enter again....")   

        elif choice == 7:
            print("Exiting.......")
            break    

        else:
            print("Invalid choice. Please try again.")




