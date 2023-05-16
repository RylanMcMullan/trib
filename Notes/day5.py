x = "Cheifs stink!"
def function():
    x = "Go Bengals!"
    print(x)

function()
print(x)

def func_a():
    return func_b() * 3
def func_b():
    return func_c() * 2
def func_c():
    return 1

x = func_a()
print(x)

def func_r(x):
    if x < 5:
        print(x)
        func_r(x+1)
func_r(1)

def func_r(x):
    if x < 5:
        print(f"Going up: {x}")
        func_r(x+1)
        print(f"Going down: {x}")
func_r(1)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5))

def add_two(x):
    return x + 2
def times_three(x):
    return x * 3
def function(x):
    return add_two(times_three(x))
print(function(5))