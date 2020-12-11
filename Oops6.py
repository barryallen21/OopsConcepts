#Types of methods
# 1.instance method

class student:

    def __init__(self):
        self.m1=89
        self.m2=45
        self.m3=90

    def add(self):
        return (self.m1+self.m2+self.m3)

o1=student()

o=o1.add()
print(o)