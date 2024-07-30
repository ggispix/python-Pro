# Task 1
from abc import ABC
import math
class Figure(ABC):

    def perimeter(self):
        raise NotImplementedError('Error')


    def area(self):
        raise NotImplementedError('There is no this func')

class  Circle(Figure):
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        res = self.radius * 2 * math.pi
        print(f"Circle perimeter: {res}")

    def area(self):
        res = math.pi * (self.radius ** 2)
        print(f"Circle area: {res}")

class Rectangle(Figure):
    def __init__(self,heigth,width):
        self.heigth = heigth
        self.width = width

    def perimeter(self):
        res = 2 * (self.heigth + self.width)
        print(f"Rectangle perimeter: {res}")

    def area(self):
        res = self.width * self.heigth
        print(f"Rectangle area: {res}")

class Traingle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        res = self.a + self.b + self.c
        print(f"Triangle perimeter: {res}")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        res = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(f"Triangle area: {res}")

circle_1 = Circle(5)
rectangle_1 = Rectangle(4,6)
triangle_1 = Traingle(5,6,7)

print(circle_1,rectangle_1,triangle_1)
circle_1.perimeter()
circle_1.area()
rectangle_1.perimeter()
rectangle_1.area()
triangle_1.perimeter()
triangle_1.area()

# Task 2
from abc import ABC,abstractmethod
class MeansOfPayment(ABC):
        @abstractmethod
        def make_payment(self, amount):
            raise NotImplementedError('Error')


class CreditCard(MeansOfPayment):
    def make_payment(self, amount):
        print(f'Payment was made by credit card. Amount:{amount}')

class BankTransfer(MeansOfPayment):
    def make_payment(self, amount):
        print(f'Payment was made by bank transfer. Amount:{amount}')
class ElectronicWallet(MeansOfPayment):
    def make_payment(self, amount):
        print(f'Payment was made by electronic wallet. Amount:{amount}')


class PaymentProcessor():
    def __init__(self):
        self.methods = []

    def add_methods(self,method_name):
        self.methods.append(method_name)

    def payment(self,method_payment,amount):
        # if method_payment not in self.methods:
        #     raise ValueError('There is wrong type of payment')

        for method_name in self.methods:
            if method_name.__class__.__name__ == method_payment:
                method_name.make_payment(amount)
                return
        print(f'Payment method {method_payment} not found.')

credit_card = CreditCard()
bank_transfer = BankTransfer()
electronic_wallet = ElectronicWallet()


processor = PaymentProcessor()
processor.add_methods(credit_card)
processor.add_methods(bank_transfer)
processor.add_methods(electronic_wallet)


processor.payment("CreditCard", 100)
processor.payment("BankTransfer", 200)
processor.payment("ElectronicWallet", 300)



