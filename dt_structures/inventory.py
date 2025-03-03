class Inventory:
    def __init__(self):
        self.items={} # dictionary to store items

    def add_item(self,name,price, quantity):
            if name in self.items:
                print(f"Item {name} already exists")
                return
            self.items[name]={"quantity":quantity, "price":price}
            print(f"Added {name} to the cart.")

    def update_quantity(self, name, new_price, new_quantity):
        if name in self.items:
            self.items[name]={"quantity":new_quantity, "price":new_price}
            print(f"Updated quantity {name} to {new_quantity} and price of {new_price}.")

        else:
            print('Item not found in inventory')

    def get_item_info(self, name):
        if name in self.items:
            item=self.items[name]
            print(f"Item: {name}, Quantity: {item['quantity']}, Price: ${item['price']}")
        else:
            print(f"Item '{name}' not found in inventory.")

inventory=Inventory()

inventory.add_item("Laptop",10,1200)
inventory.add_item("Mouse",2,10)
inventory.add_item("Monitor",5,100)
inventory.add_item("Keyboard",25,500)
inventory.add_item("Ip Phomes",17,2200)

inventory.get_item_info("Monitor")

inventory.update_quantity("Mouse",5,30)
inventory.get_item_info("Mouse")

inventory.get_item_info("Headphones")
inventory.add_item("Mouse",30,12)

