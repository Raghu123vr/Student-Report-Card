#This is a Student report card project using oops concept in python , here i created two classes namely Student adn ReportCard.

class Student:
    def __init__(self,name,roll_no):#In Student class attribute i created name,roll_no parameters
        self.name = name
        self.roll_no = roll_no
        self.marks ={}   #marks are stored in the dictionaries
    def add_marks(self,subject,marks):#In add_marks method i created subject and marks parameters
        self.marks[subject]=marks #subject are stored in keys and marks are stored in values
    def calculate_average(self):
        total=0
        for marks in self.marks.values():
            total+=marks
        average=total/len(self.marks) #calculated the average by providing total marks divided by number of marks in subjects
        print(f"{self.name} his total average or percentage is {average}")
    def is_passed(self):#In this method we know the student is passed or not
        has_passed = all(mark>=35 for mark in self.marks.values())
        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")
    def calculate_grade(self):#In this method we know the grade about student average
        percentage=sum(self.marks.values())/len(self.marks.values())
        if percentage>=85:
            print("Grade : Distinction")
        elif 60<=percentage>=84:
            print("Grade : First class")
        elif 50<=percentage>=59:
            print("Grade : Second class")
        else:
            print("Grade : Pass Class")
        
    
class ReportCard:#In this class we used static method
    def generate(self,student:Student):# inherited the class Student for this method then  generate report card
        print(f"name :{student.name}\nroll no :{student.roll_no}")
        print("subject---marks")
        for subject,marks in student.marks.items():
            print(f"{subject}---{marks}")
        student.calculate_average()
        student.is_passed()
        student.calculate_grade()
r=Student("Raghu",25)#Here i created the object and provided the required arguments
r.add_marks("maths",91)
r.add_marks("physics",96)
r.add_marks("biology",94)
r.add_marks("chemistry",86)
r.add_marks("english",85)
r.add_marks("kannada",86)
s=ReportCard()
s.generate(r)