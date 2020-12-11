# Method Overriding

class A:

    def set(self):
        print("i am barry")

class B(A):

    def set(self):
        print("i am barry allen")

o1=B()
o1.set()