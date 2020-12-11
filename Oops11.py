#Duck Typing (2)
class total:

    def __init__(self):
        self.a=90
        self.b=78

    def add(self):
        print(self.a+self.b)


class sum:

    def __init__(self):
        self.a = 90
        self.b = 23

    def add(self):
        print(self.a + self.b)


def show(d):
    d.add()

o2=sum()

show(o2)
