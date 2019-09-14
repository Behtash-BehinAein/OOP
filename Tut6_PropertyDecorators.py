# Data:    Attributes
# Methods: Functions 
# This is used if attributes are c

import os
clear = lambda: os.system('cls')
clear()

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)  

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last  = None

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'Jim'
#emp_1.fullname = 'John Doe'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

#del emp_1.fullname

