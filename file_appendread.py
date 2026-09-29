f=open("k.txt","a+")
print("first file pointer position",f.tell())
f.write("python")
print("after write file pointer position",f.tell())

f.seek(0)
print("after file pointer change ",f.tell())
print(f.read())
f.close()


#to delete text file

# import os
# os.remove("k.txt")
# print("file is delected")