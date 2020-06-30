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
        input("There are no studentes in", student_class_selection.upper())
    else:
        print("{} in {}".format(count, student_class_selection.upper()))
        input("Press enter to continue")


'''function for printing the name of students that signed up for the class'''
def students_in_class():
    count = 0
    student_class_selection = input("Which class are you looking for?: ")
    for student in student_list:
        if student_class_selection.upper() in student.get_classes():
            count+= 1
            print("{}. {}".format(i, student.get_name()))
    if count == 0:
        input("No students found!")
        

'''function for printing out specific student information'''
def find_student():
    count = 0
    find_student = []
    student_search_input = input("Who are you looking for? ")
    for student in student_list:
        if student_search_input.title() == student.get_name():
            find_student = [student.get_name(), student.get_age(), student.get_phone(), student.get_gender(), student.get_classes()]
            count += 1
    if count == 0:
        input("No students found!")
    else:
        for i in range(len(find_student)):
            print("-", find_student[i])

def line_break():
    return print("############################################")

def add_student():
    try:
        line_break()
        new_name = input("Students name: ")
        line_break()
        ask_age = True
        while ask_age == True:
            try:
                new_age = int(input("Students age: "))
                ask_age = False
            except:
                print("Use only whole numbers!")
        line_break()
        ask_phone = True
        while ask_phone == True:
            try:
                new_phone = int(input("Students phone number: "))
                ask_phone = False
            except:
                print("Use only whole numbers!")
        line_break()
        new_gender = input("Students gender: ")
        line_break()
        i = 0
        print("Input each of the students classes on a new line: ")
        print("There are five classes")
        new_class = []
        for i in range(5):
            new_class_append = input()
            new_class.append(new_class_append.upper())
        print("Does this look right?")
        import csv
        with open('myRandomStudents.csv', 'w', newline='') as csvfile:
            writer = csv.writer(file)
            writer.writerow([new_name.title(), new_age, new_phone, new_gender.capitalize(), new_class[0], new_class[1], new_class[3], new_class[4]])
    except:
        print("Something went wrong")

student_list = []

generateStudents()

add_student()

tf = True
while tf == True:
    line_break()
    print("1. Find the number of students in a class")
    print("2. Find students in a class")
    print("3. Find a specific student")
    print("4. Add student to the roster")
    print("5. Quit")
    line_break()
    try:
        user_choice = int(input("What would you like to do? "))
        line_break()
        if user_choice == 1:
            find_class()
        elif user_choice == 2:
            students_in_class()
        elif user_choice == 3:
            find_student()
        elif user_choice == 4:
            add_student()
        else:
            sure = input("Are you sure? y/n: ")
            if sure.lower() == 'y':
                tf = False
    except:
        print("Use only numbers to operate the menu!")