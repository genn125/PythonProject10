

def super_print(f):
    m = [0]
    foo = print


a def helper(x):
        m[0] = f(m[0])
        foo(f'[{m[0]}]: {x}')
    return helper
@super_print
def print(n):
    return n + 1
###################################
def count_calls(func):
    global wrapper
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # print(f"Функция {func.__name__} вызвана {wrapper.count}-й раз")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper
@count_calls