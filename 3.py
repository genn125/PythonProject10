"""
 нашел на просторах для нумерации вызовов функции


def count_calls(func):
    global wrapper
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # print(f"Функция {func.__name__} вызвана {wrapper.count}-й раз")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper
@count_calls
"""

def count_calls(func):
    global wrapper
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # print(f"Функция {func.__name__} вызвана {wrapper.count} раз(а)")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

# МОЁ из уроков

user_profile=[{'nam':7,'comment_qt':8},{'a': 25364, 'b': 6666},{'n': 78,'comment_qty3':99}]
qwer1, qwer2, qwer3 = user_profile
@count_calls
def user_info(a,b):

    print(f'{wrapper.count} - {a}, {b}')

user_info(666,999)
user_info(a=qwer1['nam'],b=qwer1['comment_qt'])
user_info(**qwer2)
user_info(qwer3['n'],qwer3['comment_qty3'])
user_info(qwer3['n'],qwer3['comment_qty3'])

