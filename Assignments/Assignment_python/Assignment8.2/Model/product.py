class Product:
    def __init__(self,name,stock,price,location,tags):
        self.name = name
        self.stock = stock
        self.price = price
        self.location = location
        self.tags = set(tags)
    
    def value(self):
        return self.stock *self.price

    def describe(self):
        return f"Name: {self.name} | Price: {self.price} | Stocks: {self.stock} | Location: {self.location} | Tags: {', ' .join(self.tags)}"
    
    def apply_discount(self,discount):
        self.price *= (1-discount/100)
    
    def __str__(self):
        return self.describe()
        
        