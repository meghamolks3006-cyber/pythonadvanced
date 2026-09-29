#read

f=open('k.txt','r')

#read()
#return file content as string format

#readlines
#returns file content as list format

#READ
s=f.read()
print(s)
print(type(s))
f.close()

#READLINES
s=f.readlines()
print(s)
print(type(s))
f.close()