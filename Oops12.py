#operator overloading

class sum:

    def __init__(self,a):
        self.a=a

    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False


o1=sum(34)
o2=sum(39)

if o1>o2:
    print("o1 is greater")
else:
    print(("o2 is greater"))