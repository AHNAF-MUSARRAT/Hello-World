# Definition:

#A method is a function that is defined inside a class. The method can be called on an object of that class.

#Syntax of method:

class Student:
 def set student_info(self, name, roll, fatherName, motherName):

self.name name
self.roll roll
self.fatherName fatherName
self.motherName = motherName

student_1 = Student()
 student_2 = Student()



student_1.set_student_info("Rahim", 3546, "Kuddus", "Fatima")
student_2.set_student_info("Karim", 3546, "Muslem", "Muslema")

 print(student_1.name)
print(student_2.name)
print(student_1.roll)
print(student_2.roll)
print(student_1.fatherName)
print(student_2.fatherName)
print(student_1.motherName)
print(student_2.motherName)