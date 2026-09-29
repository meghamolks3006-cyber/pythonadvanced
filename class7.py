#inheritance

class parent:
    def m1(self):
        print("in parent class method m1")
    def m2(self):
        print("in parent class method m2")
p=parent()
p.m1()
p.m2()


class child(parent):
     pass
c=child()
c.m1()
c.m2()

#syntax 2
class parent:
    def m1(self):
        print("in parent class method m1")
    def m2(self):
        print("in parent class method m2")
p=parent()
p.m1()
p.m2()


class child(parent):
    def m3(self):
        print("in child class method m3")
c=child()
c.m1()
c.m2()
c.m3()


#syntax3
class parent:
    def m1(self):
        print("in parent class method m1")
    def m2(self):
        print("in parent class method m2")
p=parent()
p.m1()
p.m2()


class child(parent):
    def m1(self):
        super().m1()
        print("in child class method m1")
    def m3(self):
        print("in child class method m3")
c=child()
c.m1()
c.m2()
c.m3()
