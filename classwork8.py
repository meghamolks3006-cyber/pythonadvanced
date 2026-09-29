# # #write a program to read a text file and displays the number of lines in a file
# f = open("k.txt", "r")
# s=f.readlines()
# print(len(s))
#
# # # #write a program to display the number of words in a file
# f = open("k.txt", "r")
# s=f.read()
# print(len(s.split()))


# # #write a program to update the second line in a file
# f = open("k.txt", "r")
# s=f.readlines()
# print(s)
# s[1]="new line\n"
# f.close()
# f=open('k.txt', 'w')
# f.writelines(s)
# f.close()

# f = open("k.txt", "r")
# s = f.readlines()
# print(s)
# f.close()
#
# s[1] = "new line\n"
#
# f = open("k.txt", "w")
# f.writelines(s)
# f.close()
# # #write a program to display the last 5 lines in a file
# f = open("k.txt", "r")
# s=f.readlines()
# print(s[-5:])

# #program to search a particular word in a file
# f=open('k.txt','r')
# s=f.read()
# if("python" in s):
#     print("word is present")
# else:
#     print("not present")
#
# # #find the number of letters,digits,and spaces in a file
# f=open('k.txt','r')
# s=f.read()
# l_count=0
# s_count=0
# d_count=0
#
# for i in s:
#     if(i.isalpha()):
#         l_count+=1
#     elif(i.isdigit()):
#         d_count+=1
#     elif(i.isspace()):
#         s_count+=1
# print("letters ",l_count)
# print("digits ",d_count)
# print("spaces ",s_count)


#reverse the lines in a file
# f = open("k.txt", "r")
# s = f.readlines()
# print(s[::-1])
# f.close()



# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# # Write a Python program to:
# # Read the names from both files.
f = open("totalstudents.txt", "r")
total = f.readlines()
f.close()

# f=open("passedstudents.txt","r")
# passed=f.readlines()
# # # Find the students who did not pass.
# # # Write their names to a new file named failed_students.txt, one name per line.
# f=open("totalstudents.txt","r")
# total2=f.readlines()
# f.close()
#
# f=open("passedstudents.txt","r")
# passed=f.readlines()
# f.close()
#
# failed=[]
#
# for line in total:
#     if i not in passed:
#         failed.append(i)
# f=open("failedstudents.txt","w")
# f.writelines(failed)
# f.close()
#
# print("failed students",failed)