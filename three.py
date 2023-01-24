# from second import two
#
#
# class three(two):
#     def methodthree(self):
#         print("this method first")
#
#
# obj=three()
# obj.methodone()
# obj.methodonepart()
# obj.methodtwo()
# obj.methodthree()

# # Get username and password from user
# username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# # Define a list of valid credentials
# valid_credentials = [
#     {'username': 'user1', 'password': 'pass1'},
#     {'username': 'user2', 'password': 'pass2'},
#     {'username': 'user3', 'password': 'pass3'}
# ]
#
# # Check if the entered credentials match any in the list of valid credentials
# for credential in valid_credentials:
#     if (credential['username'] == username) and (credential['password'] == password):
#         print("Login successful!")
#         break
# else:
#     print("Invalid username or password. Please try again.")

'''class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class bus(Vehicle):
    pass


obj=bus("vinay",120,40)
print(obj.seating_capacity(50))'''


'''def student(firstname, lastname='Mark', standard='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')


# 1 positional argument
student('John')

# 3 positional arguments
student('John', 'Gates', 'Seventh')

# 2 positional arguments
student('John', 'Gates')
student('John', 'Seventh')'''

#
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     # assign default value to capacity
#     def seating_capacity(self, capacity=45):
#        return super().seating_capacity(capacity=45)
#
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.seating_capacity())

# class student:
#     def __init__(self,student_id,student_name):
#         self.student_id=student_id
#         self.student_name=student_name
#
#
#     def original_method(self,student_class):
#         self.student_class=student_class
#
#     def printall(self):
#         print(self.student_id)
#         print(self.student_name)
#         print(self.student_class)
#
# stu=student(11,"rajesh")
# stu.original_method("seventh")
# stu.printall()


student1.add_student_class("10th grade")
student1.display_attributes()



