#menudriven
def add():
    n1=int(input("enter  number"))
    n2=int(input("enter  number"))
    s=n1+n2
    print("sum is",s)
def sub():
    n1=int(input("enter  number"))
    n2=int(input("enter  number"))
    s=n1-n2
    print("sub is",s)
def mul():
    n1=int(input("enter  number"))
    n2=int(input("enter  number"))
    s=n1*n2
    print("mul is",s)
def div():
    n1=int(input("enter  number"))
    n2=int(input("enter  number"))
    s=n1/n2
    print("div is",s)


#menudriven
while(True):#infinite loop
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")

    ch=int(input("enter your choice"))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    else:
        exit()