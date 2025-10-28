LOW_STOCK = 10

class Product:
    
    def __init__(self,name,stock,price,location,tags):
        self.name = name
        self.stock = stock
        self.price = price
        self.location = location
        self.tags = set(tags)
        
    def __str__(self):
        return (f"{self.name} | Stock: {self.stock} | Price: {self.price} | Location: {self.location} | Tags: {', '.join(self.tags)}")
    
    def apply_discount(self,discount):
        self.price *= (1-discount/100)
    
class Inventory:
    
    def __init__(self):
        self.products = []
        
    def list_products(self):
        if not self.products:
            print("No product in the inventory")
            return
        print("----Product List----")
        for i,product in enumerate(self.products,start=1):
            print(f"{i}: (Stock:{product})")
        print()
        
    def low_on_stock(self):
        low_on_stock_items = [p for p in self.products if p.stock <= LOW_STOCK]
        print(low_on_stock_items)
        if not low_on_stock_items:
            print("No items are low on stocks")
            return 
        print("---Low Stock items")
        for p in low_on_stock_items:
            print(p)
            print(f"Items: {p.name}(Stock: {p.stock})")
        print()
        
    def add_product(self,product):
        self.products.append(product)
        print(f"<----Product Added Successfully!!!!---->")
        
    def update_product(self,name,new_stock):
        for p in self.products:
            if p.name.lower() == name.lower():
                p.stock += new_stock
                print(f"Stock updated {p.name} Now : {p.stock}")
                return
        print("Product not found!!!!")
    
    def delete_product(self,name):
        for p in self.products:
            if p.name.lower() == name.lower():
                self.products.remove(p)
                print("Deleted Successfully!!!!")
                return
        print("Product not found")
        
    def total_stock_price(self):
        total = sum(p.stock*p.price for p in self.products)
        print(f"Total price of the product: {total:.2f}")
        
    def apply_discount_tag(self,tag="clearence",discount=30):
        discounted_items= []
        for p in self.products:
            if tag in p.tags:
                old_price = p.price
                p.apply_discount(discount)
                discounted_items.append((p.name,old_price,p.price))
                
            if not discounted_items:
                print("Clearence items not found")
            else:
                print(f"Discount applied({discount}% OFF on '{tag}' items):")
                for name,old,new in discounted_items:
                    print(f"-{name}: {old:.2f}-> {new:.2f}")
                print()
                
def menu():
    inventory = Inventory()
    
    inventory.add_product(Product("Brush",10,30,34,"Left Shelf",{"grocery"}))
    inventory.add_product(Product("Apple",4,300,"Right Shelf",{"food","clearence"}))
    inventory.add_product(Product("Mango",6,303,"Left Shelf",{"tools","clearence"}))
    inventory.add_product(Product("Soap",1,30,"Center Shelf",{"daily"}))
    inventory.add_product(Product("Detergent",6,303,"Left Shelf",{"daily","clearence"}))
    
    while True:
        print("""
========= INVENTORY MENU =========
1. List all products
2. Show low stock warnings
3. Add new product
4. Update stock
5. Delete product
6. Print total inventory value
7. Apply 30% discount on clearance items
8. Exit
==================================
""")
        choice = input("Enter number of your chice (1-8)")
        
        if choice=="1":
            inventory.list_products()
        elif choice=='2':
            inventory.low_on_stock()
        elif choice=='3':
            name = input("Enter product name: ")
            stock = int(input("Enter stock quantity: "))
            price = float(input("Enter price: ₹"))
            location = input("Enter location (e.g., shelf-1): ")
            tags = input("Enter tags (comma separated): ").split(",")
            inventory.add_product(Product(name,stock,price,location.strip(),[t.strip() for t in tags]))
        elif choice=='4':
            name = input("Enter name of product").strip()
            new_stock = int(input("Enter name to add new_stock"))
            inventory.update_product(name,new_stock)
        elif choice=='5':
            name = input("Enter product to delete")
            inventory.delete_product(name)
        elif choice=='6':
            inventory.total_stock_price()
        elif choice=='7':
            inventory.apply_discount_tag()
        elif choice=='8':
            print("Thanks for shoping")
            break
        else:
            print("Invalid number")
            
if __name__ == "__main__":
    menu()