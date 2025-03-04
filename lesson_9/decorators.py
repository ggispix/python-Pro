# Task 1
#
# def before_after(func,user):
#     def inside_decor(a):
#         print(f'Hello,{user}')
#         b = func(a)
#         print(f'Bye,{user}')
#         return b
#     return inside_decor
# def my_func(x):
#     return '*' * x
#
# my = before_after(my_func(20),'Elmira')
# print(my)

# Task 2
# def save_in_file(func):
#     file = open("../decor_file", "w")
#     def save_func(x):
#         res = file.write(str(func(x)))
#         file.close()
#         return res
#     return save_func
#
#
# def user_func(a):
#     a *= 2
#     return a
#
# use = save_in_file(user_func(10))
# print(use)
#
# with open("../decor_file.txt", "r") as file:
#     for line in file:
#         print(line)
#
# Task 3
#
# def handle_exceptions(func):
#     def wrap(*a):
#         try:
#             func(*a)
#         except Exception as e:
#             print(f'Exeption: {e}')
#     return wrap
#
# @handle_exceptions
# def divide(a, b):
#     return a / b
#
# result = divide(5, 0)
# print(result)
#
# Task 4
#
# import time
#
# def time_decorator(func):
#     def wraper(a):
#         start = time.time()
#         func(a)
#         end = time.time()
#         print(f'This function was lasted {end - start:10f} sec')
#     return wraper
#
# @time_decorator
# def some_function(a):
#     time.sleep(2)
#     for i in range(100):
#         i+=1
#         print(a*i)


# (some_function(5))
#
#
# Task 5
#
# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler('../main.log')
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.ERROR)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# stream_handler.setLevel(logging.DEBUG)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
# def log_arguments_results(func):
#     def log_func(*args):
#         logger.info(f'created arguments:{args} ')
#         res = func(*args)
#         logger.info(f'result:{res}')
#         return res
#     return log_func
#
#
#
# @log_arguments_results
# def add_numbers(a, b):
#     return a + b
#
# my_res = add_numbers(3, 4)
# print(my_res)
#
# Task 6
#
# def limit_calls(max_calls):
#     def decorator(func):
#         def wrap(*args):
#             if quantities >= max_calls:
#                 raise ValueError(f"exceeded maximum of calls ({max_calls})")
#             quantities += 1
#             return func(*args)
#
#         quantities = 0
#         return wrap
#     return decorator
#
# @limit_calls(3)
# def some_function():
#     print("Вызов функции")
#
# some_function()
# some_function()
# some_function()
# some_function()
# some_function()

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f'{self.name} costs {self.price} UAH'
#
#
# class Cart:
#     def __init__(self):
#         self.products = []
#         self.quantities = []
#
#     def add_product(self, product, quantity=1):
#         self.products.append(product)
#         self.quantities.append(quantity)
#
#     def __str__(self):
#         return '\n'.join([f'{product} x{quantity}' for product, quantity in zip(self.products, self.quantities)])

# class PaymentProcessor():
#     def pay(self):
#         print(input('Choose payment:'))
#
#
#
# class Cash(PaymentProcessor):
#     def payment(cart, processor: PaymentProcessor):
#         total = sum(product.price * quantity for product, quantity in zip(cart.products, cart.quantities))
#         processor.pay(total)
#
#     def end(self):
#
#
# class Credit():
#     def payment(cart, processor: PaymentProcessor):
#         total = sum(product.price * quantity for product, quantity in zip(cart.products, cart.quantities))
#         processor.pay(total)
#
#
# class GooglePay():
#     def payment(cart, processor: PaymentProcessor):
#         total = sum(product.price * quantity for product, quantity in zip(cart.products, cart.quantities))
#         processor.pay(total)
#
#
#
#
# pr_1 = Product('bread', 10)
# pr_2 = Product('milk', 20)
# pr_3 = Product('meat', 100)
#
# cart = Cart()
# cart.add_product(pr_1)
# cart.add_product(pr_2, 2)
# cart.add_product(pr_3)
#
# payment =
# print(cart)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cart:
#     def __init__(self):
#         self.products = []
#         self.quantities = []
#
#     def add_product(self, product, quantity=1):
#         self.products.append(product)
#         self.quantities.append(quantity)
#
# class PaymentProcessor:
#     def pay(self, total_amount):
#         # Implement payment logic here
#         print(f"Processing payment: ${total_amount:.2f}")
#
# class Cash(PaymentProcessor):
#     def payment(self, cart):
#         total = sum(product.price * quantity for product, quantity in zip(cart.products, cart.quantities))
#         self.pay(total)
#
# # Example usage
# pr_1 = Product('bread', 10)
# pr_2 = Product('milk', 20)
# pr_3 = Product('meat', 100)
#
# cart = Cart()
# cart.add_product(pr_1)
# cart.add_product(pr_2, 2)
# cart.add_product(pr_3)
#
# cash_processor = Cash()
# cash_processor.payment(cart)
# from abc import ABC, abstractmethod
#
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f'{self.name} costs {self.price} UAH'
#
#
# class Cart:
#     def __init__(self):
#         self.products = []
#         self.quantities = []
#
#     def add_product(self, product, quantity=1):
#         self.products.append(product)
#         self.quantities.append(quantity)
#
#     def __str__(self):
#         return '\n'.join([f'{product} x{quantity}' for product, quantity in zip(self.products, self.quantities)])
#
#
# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
#
# class DebitCardProcessor(PaymentProcessor):
#     def pay(self, amount):
#         print(f'Paying {amount} using Debit Card')
#
#
# class CreditCardProcessor(PaymentProcessor):
#     def pay(self, amount):
#         print(f'Paying {amount} using Credit Card')
#
#
# class PayPalProcessor(PaymentProcessor):
#     def pay(self, amount):
#         print(f'Paying {amount} using PayPal')
#
#
# def payment(cart, processor: PaymentProcessor):
#     total = sum(product.price * quantity for product, quantity in zip(cart.products, cart.quantities))
#     processor.pay(total)
#
#
# pr_1 = Product('bread', 10)
# pr_2 = Product('milk', 20)
# pr_3 = Product('meat', 100)
#
# cart = Cart()
# cart.add_product(pr_1)
# cart.add_product(pr_2, 2)
# cart.add_product(pr_3)
#
# print(cart)
#
#
# payment_type = input('Enter payment type: ')
# if payment_type == 'debit':
#     processor = DebitCardProcessor()
# elif payment_type == 'credit':
#     processor = CreditCardProcessor()
# elif payment_type == 'paypal':
#     processor = PayPalProcessor()
#
# payment(cart, processor)