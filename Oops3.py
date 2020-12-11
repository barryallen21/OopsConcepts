class computer:

    def __init__(self):
        self.a=8
        self.b=5

    def mul(self):
        return (self.a*self.b)

    def update(self):
        self.b=7


ob1=computer()
ob2=computer()

ob2.update()

c=ob1.mul()
print(c)
d=ob2.mul()
print(d)

