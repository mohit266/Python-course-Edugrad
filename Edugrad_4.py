"""QUESTION 4:
Read the file 'test.csv' and change the Grade of Rohit's grade to A and save the file to 'test.csv'

Example -

Read -  Name,Class,Subject,Grade
        Ajay,   10, English,A
        Rohit,  9,  English,B
        Chaman, 10, English,A
        Rudra,  9,  English,C
        Rajesh, 10, English,B

Write - Name,Class,Subject,Grade
        Ajay,   10, English,A
        Rohit,  9,  English,A
        Chaman, 10, English,A
        Rudra,  9,  English,C
        Rajesh, 10, English,B

Explanation read the csv file and then store the data into local variable and again write that data using writerow function of csv module (Note: Don't forget to use
newlin='' when opening the csv file in write mode)"""

import csv
def main():
    with open('test.csv', 'w', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(["Name", "Class", "Subject", "Grade"])
        writer.writerow(["Ajay",   10, "English", "A"])
        writer.writerow(["Rohit",  9,  "English", "A"])
        writer.writerow(["Chaman", 10, "English", "A"])
        writer.writerow(["Rudra",  9,  "English", "C"])
        writer.writerow(["Rajesh", 10, "English", "B"])
    with open('test.csv', 'r') as f:
        test_csv = csv.reader(f)
    return