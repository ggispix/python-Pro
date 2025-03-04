
Task 1
def consq(number,step):
    for i in number:
        i *= step
        yield i
seq = range(10)
result = list(consq(seq, 2))
print(result)

Task 2

<<<<<<< HEAD
# def my_range(start,stop,step = 1):
#     i = start
#     while i < stop:
#         yield i
#         i += step
#
# for n in my_range(10,20):
#     print(n)
#
# #Task 3
#
# def simple_number(stop):
#     prime = { }
#     i = 2
#     for n in range(i+=1,stop -= 1)
#     while i < stop:
#         if i/1 == i and i/i == 1:
#             yield i
#             i += 1
#         else:
#             i += 1
#
# for n in simple_number(1,10):
#     print(n)
#
#
# Task 4
#
# def cubes(limit):
#     numbs = []
#     start = 2
#     for i in range(start,limit+1):
#         i = i**3
#         numbs.append(i)
#         i += 1
#     yield numbs
#
# for n in cubes(10):
#     print(n)
#
# Task 5
#
# def my_fibonacci(stop):
#     a = 1
#     b = 1
#     i = 0
#     yield a
#     yield b
#     for i in range(stop - 2):
#         a,b = b, a+b
#         yield b
#
# for n in fibonacci(10):
#     print(n)
#
# Task 6
# from datetime import datetime, timedelta
#
# def date_range(start_date, end_date):
#     current_date = start_date
#     while current_date <= end_date:
#         yield current_date
#         current_date += timedelta(days=1)
#
# start_date = datetime(2024, 7, 1)
# end_date = datetime(2024, 7, 10)
#
# for date in date_range(start_date, end_date):
#     print(date.strftime("%d.%m.%Y"))
=======
def my_range(start,stop,step = 1):
    i = start
    while i < stop:
        yield i
        i += step

for n in my_range(10,20):
    print(n)

Task 3

def simple_number(stop):
    prime = { }
    i = 2
    for n in range(i+=1,stop -= 1)
    while i < stop:
        if i/1 == i and i/i == 1:
            yield i
            i += 1
        else:
            i += 1

for n in simple_number(1,10):
    print(n)


Task 4

def cubes(limit):
    numbs = []
    start = 2
    for i in range(start,limit+1):
        i = i**3
        numbs.append(i)
        i += 1
    yield numbs

for n in cubes(10):
    print(n)

Task 5

def my_fibonacci(stop):
    a = 1
    b = 1
    i = 0
    yield a
    yield b
    for i in range(stop - 2):
        a,b = b, a+b
        yield b

for n in fibonacci(10):
    print(n)

Task 6
from datetime import datetime, timedelta

def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 7, 10)

for date in date_range(start_date, end_date):
    print(date.strftime("%d.%m.%Y"))
>>>>>>> 5f99226dcca7f2923002a67f3da6babaff4f882e


# def string_to_word(text):
#     new_text = list(text.lower().split())
#     return new_text
# def my_func(word):
#     if 'a'in word and 'b' in word:
#         return len(word)
#     else:
#         return 0
# n = input('Enter sentense:')
# words = string_to_word(n)
# print(max(words,key = my_func))





