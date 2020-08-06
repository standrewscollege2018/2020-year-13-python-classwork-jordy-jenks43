from guizero import App, Text, PushButton

app = App(title="Student Management System")

teacher_list = []

class Teacher:
    def __init___(self, tname, tclass):
        self._name = tname
        self._classes = tclass
        teacher_list.append(self)

    def get_name():
        return self._name

    def get_classes():
        return self._classes

def generateTeachers():
    import csv
    with open('teachers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            Teacher(line[0], line[1])

teacher_label = Text(app)

for teacher in teacher_list:
    teacher_label.value = teacher.get_name()

generateTeachers()

app.display()