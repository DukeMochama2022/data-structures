import json
class Item:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

    def to_dict(self):
        return {"name":self.name, "quantity":self.quantity,"price":self.price}    
    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["quantity"],data['price'])

class Inventory:
    def __init__(self,filename="inventory.json"):
        self.items={} # dictionary to store items
        self.filename=filename
        self.load_inventory()

    def add_item(self,name,price, quantity):
            if name in self.items:
                print(f"Item {name} already exists")
                return
            try:
                quantity=int(quantity)
                price=float(price)
                self.items[name]=Item(name,quantity,price)
                print(f"Added {name} to the cart.")
                self.save_inventory()
            except ValueError:
                print("Invalid quantity or price. please use numeric values.")

    def update_quantity(self, name, new_price, new_quantity):
        if name in self.items:
            try:
                new_quantity=int(new_quantity)
                self.items[name]=Item(new_price,new_quantity)
                print(f"Updated quantity {name} to {new_quantity} and price of {new_price}.")
                self.save_inventory()
            except ValueError:
                print("Invalid entry. Please use an integer.")
        else:
            print('Item not found in inventory')

    def get_item_info(self, name):
        if name in self.items:
            item=self.items[name]
            print(f"Item: {name}, Quantity: {item['quantity']}, Price: ${item['price']}")
        else:
            print(f"Item '{name}' not found in inventory.")
    
    def remove_item(self,name):
        if name in self.items:
            del self.items[name]
            print(f"Removed '{name}' from inventory.")
        else:
            print(f"Item '{name}' not found in inventory.")

    def calculate_total(self):
        total=sum(item.quantity * item.price for item in self.items.values())
        print(f"Total inventory value:${total}")

    def sort_items(self, by='name'):
        if by == 'name':
            sorted_items=sorted(self.items.values(),key=lambda item: item.name)

        elif by =='price':    
            sorted_items=sorted(self.items.values(),key=lambda item: item.price)

        elif by == 'quantity':    
            sorted_items=sorted(self.items.values(),key=lambda item: item.quantity)

        else:
            print("Invalid sorting criteria")
            return
        for item in sorted_items:
            print(f"Item: {item.name}, Quantity:{item.quantity}, Price:{item.price}")    
            

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

