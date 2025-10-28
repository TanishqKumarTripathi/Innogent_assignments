import numpy as np

class StateService:
    def __init__(self,products):
        self.products = products
    
    def avg_price(self):
        prices = np.array([p.price for p in self.products])
        return np.mean(prices) if len(prices) else 0

    def most_expensive_item(self):
        prices = np.array([p.price for p in self.products])
        return np.max(prices) if len(prices) else 0
    
    def total_item_count(self):
        stocks = np.array([p.stock for p in self.products])
        return np.sum(stocks)
    
    def total_value_per_product(self):
        return {p.name:p.price*p.stock for p in self.products}
    
    def tag_based_stats(self,tag):
        tagged = [p for p in self.products if tag in p.tags]
        if not tagged:
            print("Tagged not found")
            return 
        prices = np.array([p.price for p in tagged])
        total_values = np.array([p.price * p.stock for p in tagged])
        return np.mean(prices),np.sum(total_values)
    
    def display_stats(self,tag):
        print("\n========= INVENTORY STATISTICS =========")

        print(f"Average Price of Items: ₹{self.avg_price():.2f}")
        print(f"Most Expensive Item Price: ₹{self.most_expensive_item():.2f}")
        print(f"Total Items in Stock: {self.total_item_count()}")

        print("\nTotal Value per Product:")
        
        for name,value in self.total_value_per_product().items():
            print(f" {name}: {value:.2f}")
            
        avg,total = self.tag_based_stats(tag)
        
        if avg is not None:
            print(f"Average price: {tag}: {avg}")
            print(f"Total price: {tag}: {total}")
        else:
            print("Item not found!!!!!")
            
        print("========================================\n")
        