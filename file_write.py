#write

f=open('k.txt','w')# if file exits,it will erase the file contents
#and returns its references to f.
#else it will create a new empty file and return its reference to f

#write(string)
f.write("hello\n")
f.write("python\n")
# f.write(""" Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco
# laboris nisi ut aliquip ex ea commodo consequat.""")
f.writelines(['hello\n','world\n','hi\n','python\n'])
f.close()
#writelines(list)
