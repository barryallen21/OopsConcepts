class A:

    def __init__(self):
        print("from init A")

    def a(self):
        print("from class A")

class B:

    def __init__(self):
        print("from init B")

    def a(self):
        print("from class B")

class C(B,A):

    def c(self):
        super().a()


o2=C()
o2.c()