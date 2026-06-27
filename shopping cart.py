from abc import ABC, abstractmethod

# ---------- Base Product ----------
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_price(self):
        pass

    def __str__(self):
        return f"{self.name} - ${self.get_price():.2f}"


# ---------- Derived Products ----------
class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_fee):
        super().__init__(name, price)
        self.shipping_fee = shipping_fee

    def get_price(self):
        return self.price + self.shipping_fee


class DigitalProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount  # percentage

    def get_price(self):
        return self.price * (1 - self.discount / 100)


class GroceryProduct(Product):
    def __init__(self, name, price, tax):
        super().__init__(name, price)
        self.tax = tax  # percentage

    def get_price(self):
        return self.price * (1 + self.tax / 100)


# ---------- Shopping Cart ----------
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)

    def show_cart(self):
        print("\n🛒 Shopping Cart Items:")
        for item in self.items:
            print(item)
        print(f"\n💰 Total: ${self.calculate_total():.2f}")


# ---------- Main Program ----------
if __name__ == "__main__":
    cart = ShoppingCart()

    laptop = PhysicalProduct("Laptop", 1000, 50)
    ebook = DigitalProduct("Python E-Book", 40, 20)
    apple = GroceryProduct("Apples", 10, 5)

    cart.add_product(laptop)
    cart.add_product(ebook)
    cart.add_product(apple)

    cart.show_cart()
