# Task 1

def your_sequence(func):

    def step_by_step(start,stop):
        res = func(start, stop)
        for i in res:
            yield i
    return step_by_step

def my_seq(a,b):
    x =[]
    for i in range(a,b):
        i *= 2
        x.append(i)
    return x


my_seq = your_sequence(my_seq)
for n in my_seq(1,11):
    print(n)


OR



def your_sequence(func,start,stop):
    def step_by_step(start,stop):
        current = start
        count = 0
        while count < stop:
            try:
                yield func(current)
                current += 1
                count += 1
            except StopIteration:
                break
    return step_by_step(start,stop)

def my_seq(x):
    return x ** 2

seq = your_sequence(my_seq,1,10)
for value in seq:
    print(value)

Task 2

def memorization(func):
    memory = dict()
    def inside(*args):
        if args in memory:
            return memory[args]
        else:
            memory[args] = func(*args)
            return memory[args]
    return inside
def my_fibonacci(n):
    if n <= 1:
        return n
    return my_fibonacci(n-1) + my_fibonacci(n-2)

fib = memorization(my_fibonacci(10))

for value in fib:
    print(value)


Task 3

def your_func(any_list):
    storage = []
    def wrap(user_func):
        for i in any_list:
            wr = user_func(i)
            storage.append(wr)
        yield sum(storage)
    return wrap

def user_func(a):
    a *= 2
    return a
my_list = [1,2,3,4,5,6,7,8,9]
user = your_func(my_list)(user_func)

for n in user:
    print(n)



