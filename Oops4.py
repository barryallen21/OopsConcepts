#constructor and self

class computer:

    def __init__(self):
        self.a=8
        self.b=5

    def mul(self):
        return (self.a*self.b)


    def compare(self,d):
        if self.b==d.b:
            return True
        else:
            return False

ob1=computer()
ob2=computer()

ob2.b=3
c=ob1.mul()
print(c)
d=ob2.mul()
print(d)

if ob1.compare(ob2):
    print("the nos are same")
else:
    print("not same")
