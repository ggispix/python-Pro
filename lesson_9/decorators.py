Task 1

def before_after(func,user):
    print(f'Hello,{user}')
    def inside_decor(a):
        b = func(a)
        print(f'Bye,{user}')
        return b
    return inside_decor

def my_func(x):
    return '*' * x

my = before_after(my_func(20),'Elmira')

Task 2
def save_in_file(func):
    file = open("../decor_file", "w")
    def save_func(x):
        res = file.write(str(func(x)))
        file.close()
        return res
    return save_func


def user_func(a):
    a *= 2
    return a

use = save_in_file(user_func(10))
print(use)

with open("../decor_file.txt", "r") as file:
    for line in file:
        print(line)

Task 3

def handle_exceptions(func):
    def wrap(*a):
        try:
            func(*a)
        except Exception as e:
            print(f'Exeption: {e}')
    return wrap

@handle_exceptions
def divide(a, b):
    return a / b

result = divide(5, 0)
print(result)

Task 4

import time

def time_decorator(func):
    def wraper(a):
        start = time.time()
        func(a)
        end = time.time()
        print(f'This function was lasted {end - start:10f} sec')
    return wraper

@time_decorator
def some_function(a):
    for i in range(100):
        i+=1
        print(a*i)


(some_function(5))


Task 5

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('../main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
def log_arguments_results(func):
    def log_func(*args):
        logger.info(f'created arguments:{args} ')
        res = func(*args)
        logger.info(f'result:{res}')
        return res
    return log_func



@log_arguments_results
def add_numbers(a, b):
    return a + b

my_res = add_numbers(3, 4)
print(my_res)

Task 6

def limit_calls(max_calls):
    def decorator(func):
        def wrap(*args):
            quantities = 0
            if quantities >= max_calls:
                raise ValueError(f"exceeded maximum of calls ({max_calls})")
            quantities += 1
            return func(*args)
        return wrap
    return decorator

@limit_calls(3)
def some_function():
    print("Вызов функции")

some_function()
some_function()
some_function()
some_function()
some_function()



