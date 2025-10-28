from Model.product import Product
from constant import LOW_STOCK
from Service.Stats_Service import StateService

class inventory_mangment:
    def __init__(self):
        self.products =[]
        
    def show_stats(self,tag):
        if not self.products:
            print("Notihng to sohw in inventory")
            return
        stats = StateService(self.products)
        stats.display_stats(tag)
    
    def add_product(self,product:Product):
        self.products.append(product)
        print("<----Added Successfully---->")
    
    def list_product(self):
        if not self.products:
            print("Inventory is Emply Add Items!!!!")
            return
        print("<----Products---->")
        
        for i,product in enumerate(self.products,start=1):
            print(f"{i}: {product}")
        print()
        
    def low_on_stock(self):
        low_stock = [p for p in self.products if p.stock<=LOW_STOCK ]
        
        if not low_stock:
            print("Now items are low in stocks!!!!!")
        print("<---Low Stocks Items--->")
        for p in low_stock:
            print(f"{p.name}: Stocks: {p.stock}")
    
    def update_stock(self,name,new_stock):
        for p in self.products:
            if p.name.lower() == name.lower():
                p.stock += new_stock
                print(f"Updated stocks {p.name} to {p.stock}")
                return
        print("Item not present")            
        
    def delete_product(self,name):
        for p in self.products:
            if p.name.lower() == name.lower():
                self.products.remove(p)
                print(f"{name} product deleted successfully")
                return
        print("Product not found")
        
    def total_stock(self):
        total = sum(p.value() for p in self.products)
        print(f"total price of product with stock {total:.2f}")
        
    def apply_discount(self,tag="clearence",discount=30):
        discounted_items = []
        
        for p in self.products:
            if tag in p.tags:
                old_price = p.price
                p.apply_discount(discount)
                discounted_items.append((p.name,old_price,p.price))
                
        if not discounted_items:
            print("Tag {tag} not found!!!!")
        else:
            print("<-----Discounted Item----->")
            for name,old,new in discounted_items:
                print(f"{name} old price: {old} new price: {new}")
                
        
        