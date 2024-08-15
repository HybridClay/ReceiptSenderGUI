#This is to get all files in the Downloads folder directory and 
#get the name part of the pdf's. Have only files, NO folders in Downloads folder directory

import os
import shutil

pdf = (".pdf")

def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

#For Windows
#os.chdir('C:/Users/UserNameHere/Downloads')
#For Mac
os.chdir('/Users/akv/Downloads')


#This just prints EVERY file in directory
for file in os.listdir():
    print(file)

print("-----------------------")
#This just returns True or False if the files in directory are pdf files
for file in os.listdir():
    print(is_pdf(file))

print("-----------------------")
#This prints out files in directory that are pdf files only
for file in os.listdir():
    if is_pdf(file):
        print(file)

print("-----------------------")
#This splits the file name by the dash line "-" and we print the forst part of the splittes string
for file in os.listdir():
    if is_pdf(file):
        print(file.split("-")[0])

print("-----------------------")
#An alternative of the same as above, except its goinng backwards in index number
for file in os.listdir():
    if is_pdf(file):
        print(file.split("-")[-2])
print("-----------------------")
