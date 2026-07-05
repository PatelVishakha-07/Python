""" 
The Spice Route’s dinner rush peaks at 300 orders per hour and the hand-written KOT (Kitchen Order Ticket) system has collapsed. You are hired to build the core order engine in Python. Business rules: every menu item has a name and base price; Food items attract 5% GST; Beverage items attract 12% GST; any item flagged as a ‘Chef’s Special’ carries a 10% premium on the base price before tax. At closing time, the day’s orders must be saved to disk so accounts can audit them the next morning.

(a)  Design a class hierarchy: an abstract/base class MenuItem with subclasses Food and Beverage. Each must expose a method final_price() computed polymorphically according to the rules above. Implement it in Python (use of @property, __init__ chaining via super(), and method overriding will be credited).

 """

from abc import ABC, abstractmethod

class MenuItem(ABC):

    def __init__(self, name, price, chef_special=False):
        self._name = name
        self._base_price = price
        self._chef_special = chef_special

    @property
    def name(self):
        return self._name
    
    @property
    def base_price(self):
        return self._base_price
    
    @property
    def chef_special(self):
        return self._chef_special

    @abstractmethod
    def final_price(self):
        pass

class Food(MenuItem):
    gst = 0.05

    def __init__(self, name, price, chef_special=False):
        super().__init__(name, price, chef_special)

    def final_price(self):
        price = self.base_price

        if self.chef_special:
            price *= 1.10

        price *= (1 + Food.gst)
        return round(price, 2)
    
class Beverages(MenuItem):
    gst = 0.12

    def __init__(self, name, price, chef_special=False):
        super().__init__(name, price, chef_special)

    def final_price(self):
        price = self.base_price

        if self.chef_special:
            price *= 1.10

        price *= (1 + Beverages.gst)

        return round(price, 2)
    

class Order:

    def __init__(self):
        self.items = []

    def add_items(self, name):
        self.items.append(name)

    def total(self):
        total = sum(item.final_price() for item in self.items)

        return self.__apply_discount(total)
    
    def __aply_discount(self, amount):
        if amount > 2000:
            amount *= 0.10
        return round(amount, 2)
    
    def to_dict(self):
        return{
            "items":[
                {
                    "type": item.__class__.__name__,
                    "name": item.name,
                    "base_price": item.base_price,
                    "chef_special": item.chef_special
                 }
                for item in self.items
            ]
        }
