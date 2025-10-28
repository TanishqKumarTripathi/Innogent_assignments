from Model.product import Product
from Model.food_product import FoodProduct
from Service.inventory_mangment import inventory_mangment
from datetime import date

def menu(): 
    inventory = inventory_mangment()
    
    inventory.add_product(Product("Brush", 10, 30, "Left Shelf", ["grocery"]))
    inventory.add_product(FoodProduct("Apple", 4, 300, "Right Shelf", ["food","clearence"], date(2025,12,31)))
    inventory.add_product(Product("Soap", 1, 30, "Center Shelf", ["daily"]))
    inventory.add_product(Product("Brush", 10, 30, "Left Shelf", ["grocery"]))
    inventory.add_product(Product("Soap", 5, 25, "Center Shelf", ["daily"]))
    inventory.add_product(Product("Shampoo", 8, 150, "Top Shelf", ["personal care"]))
    inventory.add_product(Product("Toothpaste", 3, 60, "Right Shelf", ["daily", "clearence"]))
    inventory.add_product(Product("Detergent", 6, 120, "Left Shelf", ["cleaning"]))
    
    inventory.add_product(FoodProduct("Apple", 4, 300, "Right Shelf", ["food", "clearence"], date(2025, 12, 31)))
    inventory.add_product(FoodProduct("Mango", 10, 250, "Left Shelf", ["food"], date(2025, 11, 30)))
    inventory.add_product(FoodProduct("Bread", 2, 40, "Bottom Shelf", ["food", "baked"], date(2025, 10, 30)))
    inventory.add_product(FoodProduct("Milk", 1, 60, "Fridge Section", ["dairy"], date(2025, 10, 29)))
    inventory.add_product(FoodProduct("Cheese", 7, 200, "Fridge Section", ["dairy"], date(2025, 11, 10)))
    
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
8. Show Statistics
9. Exit
==================================
""")
        
        choice = input("Choose a number (1-8)")
        
        if choice=='1':
            inventory.list_product()
        elif choice=='2':
            inventory.low_on_stock()
        elif choice=='3':
            name = input("Enter product name: ")
            stock = int(input("Enter stock quantity: "))
            price = float(input("Enter price: "))
            location = input("Enter location: ")
            tags = input("Enter tags (comma separated): ").split(",")
            is_food = input("Is this a food product? (y/n): ").lower()
            
            if is_food == "y":
                year = int(input("Enter Year: "))
                month = int(input("Enter Month: "))
                day = int(input("Enter Date: "))
                expiry = date(year,month,day)
                inventory.add_product(FoodProduct(name,stock,price,location,[t.strip() for t in tags],expiry))
            else:
                inventory.add_product(Product(name,stock,price,location,[t.strip() for t in tags]))
        elif choice=='4':
            name = input("Enter item name to update: ")
            stocks = input("Enter stocks: ")
            inventory.update_stock(name,stocks)
        elif choice=='5':
            name = input("Enter product name to delete")
            inventory.delete_product()
        elif choice=='6':
            inventory.total_stock()
        elif choice=='7':
            inventory.apply_discount()
        elif choice=='8':
            print("Thanks for shopping !!!!!!")
        else:
            print("Invalid Number")
            
if __name__ == "__main__":
    menu()