
# Цикл for in

def dict_to_list(my_dict):
    list_1 = []
    for k, v in my_dict.items():
        if isinstance(v,int):
            v *= 2
        list_1.append((k,v))
    return list_1

print('1 -', dict_to_list({'a': 15, 'b': 2.4, 'c': [], 'd':'asd','e': 395}))


def filter_to_list(mlist_to_filter, value_type):
    list_2 = []
    for i in mlist_to_filter:
        if type(i)==value_type:
            list_2.append(i)

        # if isinstance(i,value_type):      # Не рекомендуется, так как True тоже входит в int
        # list_2.append(i)

    return list_2

print('2 -', filter_to_list([35,True, 'asd',10],int))
print('3 -', filter_to_list([35,True, 'asd',10],str))
print('4 -', filter_to_list([35,True, 'asd',10],bool))

#
# '''
# Используя лямбда функцию
# '''
#
# def filter_to_list(list_to_filter, value_type):
#     return list(filter(lambda elem: type(elem) is  value_type ,list_to_filter))
#
#       # def check_element_type(elem):
#       #     return type(elem) is value_type
#       #   return isinstance(elem,value_type)      # Не рекомендуется, так как True тоже входит в int
#       # return list(filter(check_element_type, list_to_filter))
#
# print('5 -', filter_to_list([35,True, 'asd',10, 5.5],int))
# print('6 -', filter_to_list([35,True, 'asd',10, 5.5],float))
# print('7 -', filter_to_list([35,True, 'asd',10, 5.5],str))
#



