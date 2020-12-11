
class add:


    def show(self,a,b):
        print(a+b)

class mul:

    def show(self,a,b):
        print(a*b)

def get(other):
    other.show(34,56)

o1=add()
o2=mul()

get(o1)
get(o2)

