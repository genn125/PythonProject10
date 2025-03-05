#  Создание ошибок

def image_info (kwargs):
    if ('image_id' not  in kwargs) or ('image_title' not  in kwargs):
        raise TypeError('Ошибка')
    return f'Image "{kwargs['image_title']}" has id {kwargs['image_id']}'

try:
    print(image_info ({'image_title': 'my cat', 'image_id': 123}))
    print(image_info ({'image_title': 'my cat'}))
except TypeError as e:
    print(e)

