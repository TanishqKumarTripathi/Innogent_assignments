from .product import Product as pd
from datetime import date

class FoodProduct(pd):
     
    def __init__(self, name, stock, price, location, tags,expirydate):
          super().__init__(name, stock, price, location, tags)
          self.expirydate = expirydate

    def describe(self):
        base_desc = super().describe()
        return f"{base_desc} | Expiry: {self.expirydate}"
    
    def is_expired(self):
        return self.expirydate < date.today()
