def func(x):
    return x * 3
new_func = func

def func(x):
    return x + 2

print(new_func(2))