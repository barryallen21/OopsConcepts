#init method

class com:

    def __init__(self,l,app):
        self.l=l
        self.app=app

    def lan(self):
        print("the lang is:{0} & used for:{1}".format(self.l,self.app))

ob1=com("java","mobile apps")
ob2=com("python","data science")
ob1.lan()
ob2.lan()

