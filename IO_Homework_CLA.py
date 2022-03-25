#open file
file = open('D:\python temporary\IO Homework CLA\student_names.txt')
student_list = file.read()
#Write random names
student_list=student_list+"\nBELKHIR Sami"+"\nBOUABDELLAH Samir"+"\nAHMED Yanis"+"\nBAOUCHI Yahia"
file = open('D:\python temporary\IO Homework CLA\student_names.txt','w')
file.write(student_list)
print(student_list)
file.close()
#Print first n lines with n=2
file = open('D:\python temporary\IO Homework CLA\student_names.txt')
content = file.readlines()
print(content[:2])
#Print the last n lines with n=2
content_last = file.readlines()
print(content[-2:])
#Check if the name x is in the file, in this case x='AHMED Yanis'
print('AHMED Yanis' in student_list)
#Write a Python program to generate 26 text files 
#named A.txt, B.txt, and so on up to Z.txt.
#Making a list containing all capital letters
import string
letters_string=string.ascii_uppercase
Letters=[]
for i in range(26):
    Letters.append(letters_string[i])
print(Letters)
#Creating the files
for i in range(26):
    open('{}.txt'.format(Letters[i]),'w')