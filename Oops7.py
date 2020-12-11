#Types of methods
# 2.class method

class student:

    m1,m2,m3=89,90,76

    @classmethod
    def add(cls):
        return (cls.m1+cls.m2+cls.m3)

o1=student()

sum=student.add()
print(sum)
