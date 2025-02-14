
# Классы и экземпляры

class Image:

    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize (self, res):
        self.resolution = res

    def __str__(self):
        return f'{self.title}.{self.extension}'

    @staticmethod
    def tyu (a,b):
        return f'{a} {b}'

first_img = Image('200x400', 'fig1', 'jpg')
zxc = Image('1920x1080', 'fig2', 'png')

print(first_img.resolution)
print(first_img.title)
print(first_img.extension)
print("__________")
first_img.resize('2x2')
print(first_img.resolution)
print(first_img)
print(first_img.tyu(123, 567))

zxc.resize('3840x2160')
print(zxc.resolution)
print(zxc.title)
print(zxc.extension)
print(zxc)

# def super_print(f):
#     m = [0]
#     foo = print
#
#     def helper(x):
#         m[0] = f(m[0])
#         foo(f'[{m[0]}]: {x}')
#
#     return helper



