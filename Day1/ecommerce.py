# Abstraction
from abc import ABC, abstractmethod           # Abstract Base Class


class Paymentprocess(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Encapsulation


class Product:
    def __init__(self, name, price, stock):
        self.name = name          # public attribute
        self.__price = price        # private attribute
        self._stock = stock    # protected attribute

    def get_price(self):          # getter method for private attribute
        return self.__price

    def set_price(self, price):   # setter method for private attribute
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than zero.")

    def display_info(self):
        print("Product: ", self.name, ", Price:",
              self.__price, ", Stock: ", self._stock)


# Inheritance
class Clothing(Product):
    def __init__(self, name, price, stock, size, material):
        super().__init__(name, price, stock)
        self.size = size
        self.material = material

    def display_info(self):
        super().display_info()
        print(" Size: ", self.size, ", Material: ", self.material)


class Electronics(Product):
    def __init__(self, name, price, stock, brand, warranty):
        super().__init__(name, price, stock)
        self.brand = brand
        self.warranty = warranty

    def display_info(self):
        super().display_info()
        print(" Brand: ", self.brand, ", Warranty: ", self.warranty)


class Grocery(Product):
    def __init__(self, name, price, stock, expiration_date):
        super().__init__(name, price, stock)
        self.expiration_date = expiration_date

    def display_info(self):
        super().display_info()
        print(" Expiration Date: ", self.expiration_date)

# Polymorphism


class CreditCardPayment(Paymentprocess):
    def pay(self, amount):
        print("Making credit card payment of", amount)
        print("Processing credit card payment...")
        print("Credit card payment of", amount, "successful.")


class PayPalPayment(Paymentprocess):
    def pay(self, amount):
        print("Making PayPal payment of", amount)
        print("Processing PayPal payment...")
        print("PayPal payment of", amount, "successful.")


class BankTransferPayment(Paymentprocess):
    def pay(self, amount):
        print("Making bank transfer payment of", amount)
        print("Processing bank transfer payment...")
        print("Bank transfer payment of", amount, "successful.")


print("E-commerce module loaded.")
cart_value = 0
while True:
    print("1. Clothing\n2. Electronics\n3. Grocery\n4. Exit\n")
    choice = int(input("Select product category (1-3): "))
    if choice == 1:
        clothe = input("Enter clothing name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        size = input("Enter size: ")
        material = input("Enter material: ")
        product = Clothing(clothe, price, stock, size, material)
        cart_value += product.get_price()
    elif choice == 2:
        electronic = input("Enter electronic item name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        brand = input("Enter brand: ")
        warranty = input("Enter warranty period: ")
        product = Electronics(electronic, price, stock, brand, warranty)
        cart_value += product.get_price()
    elif choice == 3:
        grocery = input("Enter grocery item name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        expiration_date = input("Enter expiration date: ")
        product = Grocery(grocery, price, stock, expiration_date)
        cart_value += product.get_price()
    elif choice == 4:
        print("Exiting...")
        break

print("Choose payment method:")
print("1. Credit Card\n2. PayPal\n3. Bank Transfer")
payment_choice = int(input("Select payment method (1-3): "))
if payment_choice == 1:
    payment = CreditCardPayment()
    payment.pay(cart_value)
elif payment_choice == 2:
    payment = PayPalPayment()
    payment.pay(cart_value)
elif payment_choice == 3:
    payment = BankTransferPayment()
    payment.pay(cart_value)

print("Thanks for shopping with us!")


# laptop = Electronics("Laptop", 1200, 10, "Dell", "2 years")
# laptop.display_info()
# print("After price update:")
# laptop.set_price(1100)
# laptop.display_info()

# print("Buying cloths: ")
# tshirt = Clothing("T-Shirt", 20, 50, "L", "Cotton")
# tshirt.display_info()

# # Cart value
# cart_value = laptop.get_price() + tshirt.get_price()

# payment = PayPalPayment()
# payment.pay(cart_value)
