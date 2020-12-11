#Duck Typing

class A:

    def barry(self):
        print("i am barry from class A")

class B:

    def barry(self):
        print("i am barry from class B")

class C:
    def check(self,arg):
        arg.barry()

o1=A()
o2=B()
o3=C()

o3.check(o2)
o3.check(o1)
