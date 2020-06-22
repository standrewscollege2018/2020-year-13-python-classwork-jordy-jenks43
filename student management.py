'''this program is able to manage a student data base'''

class Student:
    '''the student class stores student's name, age phone number, if they are enrolled, gender, and a list of their classes'''
    
    '''setting up all attributes for students within the list from the student csv file'''
    def __init__(self, name, age, phone, gender, classes):
        self._name = name
        self._age = age
        self._phone = phone
        self._gender = gender
        self._classes = classes
        self.enrolled = True
        student_list.append(self)
    
    '''getter function for getting student names'''
    def get_name(self):
        return self._name
    
    '''getter function for student age'''
    def get_age(self):
        return self._age
    
    '''getter function for phone numbers'''
    def get_phone(self):
        return self._phone
    
    '''getter function for student enrollment status'''
    def get_enrolled(self):
        return self._enrolled
    
    '''getter function for student genders'''
    def get_gender(self):
        return self._gender
    
    '''getter function for student enrolled class'''
    def get_classes(self):
        return self._classes

'''generating the students via custom function'''
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

'''function for finding the number of students enrolled to a subject'''
def find_class():
    student_class_selection = input("What class are you looking for?: ")
    count = 0    
    for student in student_list:
        if student_class_selection.upper() in student.get_classes():
            count += 1
    if count == 0:
        print("There are no students in this class!")
    else:
        print(count)    

'''function for printing the name of students that signed up for the class'''
def students_in_class():
    student_class_selection = input("Which class are you looking for?: ")
    for student in student_list:
        if student_class_selection.upper() in student.get_classes():
            print(student.get_name())

'''function for printing out specific student information'''
def find_student():
    student_search_input = input("Who are you looking for? ")
    for student in student_list:
        if student_search_input.title() == student.get_name():
            print(student.get_name())
            print(student.get_age())
            print(student.get_phone())
            print(student.get_gender())
            print(student.get_classes())

student_list = []

generateStudents()
find_student()