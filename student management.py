'''this program is able to manage a student data base'''

def generateStudents():
    import csv
    with open ('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes = []
            i = 4
            while i in range(4,9):
                classes.append(line[i])
                i += 1
            Student(line[0], int(line[1]), line[2], line[3], classes)

class Student:
    '''the student class stores student's name, age phone number, if they are enrolled, gender, and a list of their classes'''
    
    def __init__(self, name, age, phone, gender, classes):
        self._name = name
        self._age = age
        self._phone = phone
        self._gender = gender
        self._classes = classes
        student_list.append(self)
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_phone(self):
        return self._phone
    
    def get_enrolled(self):
        return self._enrolled
    
    def get_gender(self):
        return self._gender
    
    def get_classes(self):
        return self._classes

student_list = []

generateStudents()

print(student.get_classes())

'''
student_class_selection = input("Input a class: ")
count = 0

for student in student_list:
    if student_class_selection.lower() in student.get_classes():
        count += 1

print(count)
'''