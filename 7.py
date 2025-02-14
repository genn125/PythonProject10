
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

first_img = Image('200x400', 'fig1', 'jpg')

print(first_img.resolution)
print(first_img.title)
print(first_img.extension)
print()
first_img.resize('2x2')
print(first_img.resolution)
print(first_img)

zxc = Image('1920x1080', 'fig2', 'png')
# zxc.resize('3840x2160')
# print(zxc.resolution)