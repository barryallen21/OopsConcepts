#types of variables

class lan:

    current_lan="python"       #static/class var

    def __init__(self):         #instance var
        self.a="c#"
        self.b="java"

o1=lan()
o2=lan()

o1.a="js"
lan.current_lan="c"

print(o1.a,o1.b,lan.current_lan)
print(o2.a,o2.b)