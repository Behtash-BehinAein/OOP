# Data:    Attributes
# Methods: Functions 
# Class variables vs instance variables 

import os
clear = lambda: os.system('cls')
clear()

class Employee:

    num_of_employees = 0
    raise_amount = 1.04  # Class variable: can be the same across all instances or specific to instances
                            # This can be acheived via using self.<variable> vs <class name>.<variable>

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first  + '.' + last + '@company.com' 

        Employee.num_of_employees += 1 

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 


    def apply_raise(self):
        #self.pay  = int(self.pay * Employee.raise_amount)  # will set the variable to be the same across all instances
        self.pay  = int(self.pay * self.raise_amount)       # Can change the class variable for each instance if desired


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


# print(emp_1.__dict__)

'''
Employee.raise_amount = 1.05


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''
'''
# --------------------------
emp_1.raise_amount = 1.05


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''


print(Employee.num_of_employees)