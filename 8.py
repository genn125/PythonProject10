
# Магические методы в классах

class Comment:
    def __init__(self, text,tr_comment):
        self.text = text
        self.votes_qty = 0
        self.tr_comment=tr_comment
    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other, tr_comment):
        return f'{self.text} + {other.text}', self.votes_qty + other.votes_qty + tr_comment.votes_qty

first_comment = Comment('Первый комментарий')
first_comment.upvote()

second_comment = Comment('Второй комментарий')
second_comment.upvote()

tr_comment = Comment('3 комментарий')
tr_comment.upvote()


print(first_comment + second_comment)