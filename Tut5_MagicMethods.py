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

    # 1
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

    # 2
    def __repr__(self):
        return 'Employee({} , {} , {})'.format(self.first, self.last, self.pay)

    # 3
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

# ======================================================================================================================


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Doe', 50000)

print(len(emp_1))

print(repr(emp_1))
print(str(emp_1))
