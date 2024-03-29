# Data:    Attributes
# Methods: Functions 
import os
clear = lambda: os.system('cls')
clear()

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first  + '.' + last + '@company.com' 

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


#print(emp_1)
#print(emp_2)


print(emp_1.email)
print(emp_2.email)


# These 2 lines are the same 
print(emp_1.fullname())
print(Employee.fullname(emp_1))


