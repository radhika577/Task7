# class MathematicalOperations:
#     # withou input and without return add two numbers
#     @staticmethod
#     def add():
#         a=10
#         b=20
#         print("Sum =",a +b)
#     #with input and without return substract two numbers
#     @staticmethod
#     def subtract(n1,n2):
#         print("Sub =",n1-n2)
#     # without input and with return divide two numbers
#     @staticmethod
#     def division():
#         x=10
#         y=20
#         z=30
#         avg=(x+y+z)/3
#         return avg
#     # with input and with return multiply 4 numbers
#     @staticmethod
#     def multiply(a,b,c,d):
#         return a*b*c*d 
# MathematicalOperations.add()
# MathematicalOperations.subtract(20,10)
# print(MathematicalOperations.division())
# print(MathematicalOperations.multiply(1,2,3,4))


# class Test:
#     def myMethod(self):
#         print("I am a Instance Method")
# t1=Test()
# t1.myMethod()

# class VariableEx:
#     name="Hero"
#     @staticmethod
#     def m1():
#         print("I am m1 =",VariableEx.name)

#     @staticmethod
#     def m2():
#             print("I am m2 =",VariableEx.name)

# VariableEx.m1()
# VariableEx.m2()

# class Test:
#     name="Hero"

# class Abc:
#     @staticmethod
#     def m1():
#         print("M1 from Abc here Name =",Test.name)
# Abc.m1()

        
# class Test:
#     def m1(self):
#         self.name="Zero"
#         print("I am a instance Method m1 Name = ",self.name)

#     def m2(self):
#         print("I am a instance Method m2 Name = ",self.name)
# t1=Test()
# t1.m1()
# t1.m2()

# class Test:
#     def m1(self):
#         self.name="Zero"
# t=Test()
# t.m1()
# class Test2:
#     def m2(self):
#         print("Instance variable in another class",t.name)
# a=Test2()
# a.m2()


# class Test:
#     def display(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#         print("Course : ",self.course)
# t=Test()
# t.name="Hero"
# t.age=21
# t.course="python fullstack"
# t.display()


# class Student:
#     def displayDetails(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#         print("Course : ",self.course)
# std1=Student()
# std1.name="Hero"
# std1.age=21
# std1.course="python fullstack"
# print("------------Student1------------")
# std1.displayDetails()

# std2=Student()
# std2.name="Zero"
# std2.age=23
# std2.course="Java fullstack"
# print("------------Student2------------")
# std2.displayDetails()


# class Student:
#     def assignData(self,name,age,course):
#         self.myName=name
#         self.myAge=age
#         self.myCourse=course
        
#     def displayDetails(self):
#         print("Name : ",self.myName)
#         print("Age : ",self.myAge)
#         print("Course : ",self.myCourse)
        
# s1=Student()
# s1.assignData("Hero",21,"Python")
# print("-----------Student1----------")
# s1.displayDetails()

# s2=Student()
# s2.assignData("Hero2",23,"Java")
# print("-----------Student2----------")
# s2.displayDetails()

# s3=Student()
# s3.assignData("Hero3",25,"DataScience")
# print("-----------Student3----------")
# s3.displayDetails()

# class Student:
#     ins_name="Innomatics"
#     def assignData(self,name,course):
#         self.myName=name
#         self.myCourse=course
#     def displayDetails(self):
#         print("My Name : ",self.myName)
#         print(" Course :  ",self.myCourse)
#         print("Institute Name : ",Student.ins_name)
# s1=Student()
# s1.assignData("Hero","Python")
# s1.displayDetails()

# s2=Student()
# s2.assignData("Zero","Data Science")
# s2.displayDetails()

# MOVIE
# class Movie:
#     movie_lang="Telugu"
#     def assignData(self,movie_name,hero,genre):
#         self.movie_name=movie_name
#         self.hero=hero
#         self.genre=genre
#     def displayDetails(self):
#         print("Movie Name : ",self.movie_name)
#         print("Hero Name : ",self.hero)
#         print("Movie Genre : ",self.genre)
#         print("Movie Language : ",Movie.movie_lang)
# m1=Movie()
# m1.assignData("Jersey","Nani","Sports Drama")
# print("----------------------------------------")
# m1.displayDetails()

# m2=Movie()
# m2.assignData("Darling","Prabhas","Romantic Comedy")
# print("----------------------------------------")
# m2.displayDetails()


#Hospital
# class Hospital:
#     hsptl_name="Apollo Hospital"
#     def assignData(self,patient_name,age,disease):
#         self.patient_name=patient_name
#         self.age=age
#         self.disease=disease
#     def displayDetails(self):
#         print("Patient Name : ",self.patient_name)
#         print("Age : ",self.age)
#         print("Disease : ",self.disease)
#         print("Hospital Name : ",Hospital.hsptl_name)
# p1=Hospital()
# p1.assignData("Laxmi",52,"Diabetes")
# print("-----------------------------------------")
# p1.displayDetails()

# p2=Hospital()
# p2.assignData("Ram",28,"Migraine")
# print("-----------------------------------------")
# p2.displayDetails()


#MUSIC CONCERT
# class Music_concert:
#     venue_name="Hitex Exhibition Center"
#     def assignData(self,artist_name,ticket_price,show_time):
#         self.artist_name=artist_name
#         self.ticket_price=ticket_price
#         self.show_time=show_time 
#     def displayDetails(self):
#         print("Artist Name : ",self.artist_name)
#         print("Ticket Price : ",self.ticket_price)
#         print("Show Time : ",self.show_time)
#         print("Venue : ",Music_concert.venue_name)
# m1=Music_concert()
# m1.assignData("Anirudh",1500,"7:00 PM ")
# print("-------------------------------------------")
# m1.displayDetails()

# m2=Music_concert()
# m2.assignData("Arjith Singh",1000, "7:00 PM")
# print("-------------------------------------------")
# m2.displayDetails()

