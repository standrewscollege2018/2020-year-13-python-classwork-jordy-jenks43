'''this program is able to manage a student data base'''
import random

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
        return self.classes

student_list = []

Student("Jack", "16", "0273956577", "Male", "GRA, MAT, ENG")
Student("Hannah", "15", "0274528999", "Female", "MAT, ART")
Student("Matt", "17", "0224887765", "Male", "MAT, PHY, ART")

for student in student_list:
    print(student.get_name())
