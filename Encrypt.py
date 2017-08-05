import csv
import string
from rot import rot

student_no = []
student_name = []
letter_list = string.ascii_uppercase

## open file
data = open('studentlist.csv', 'r')
reader = csv.reader(data)

## iterate reade csv and create list
for row in reader:
    student_no.append(row[0])
    student_name.append(row[1])
n = len(student_name)

## create captialized 8 letters student name
student_name_mod = []
for i in range(n):
    student_name_mod.append(student_name[i][0:8].upper())

## create encrypted student name
student_name_encrypted = []
for i in range(n):
    student_name_encrypted.append(rot(student_name_mod[i],student_no[i],letter_list))

## write CSV file
out_file = open('out_list.csv','w',newline='')
writer = csv.writer(out_file,delimiter=',')
for i in range(n):
    writer.writerow([student_no[i],student_name[i],student_name_encrypted[i]])
out_file.close()
