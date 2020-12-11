# Method overloading

class add:

    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:
            return (a+b+c)

        elif a!=None and b!=None:
            return (a+b)

        else:
            return (a)

o1=add()

print(o1.sum(2,8,5))
