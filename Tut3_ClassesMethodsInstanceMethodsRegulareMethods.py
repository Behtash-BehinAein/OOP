# Data:    Attributes
# Methods: Functions 
# Class variables vs instance variables 
# Regular method, class methods and instance methods 

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



    @classmethod  # You can change a class variable with this method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    # Alternative constructor: you can perfrom the same operation for all instances. Could be in the init method as well. 
    # But it looks like that is more reseved for instance variables 
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    # Static methods: they have some logical connections with the class. Very much like a function. 
    # It will not take any 'cls' or 'self' argument. 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



# End of class ==========================================================================================================

import datetime 
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


# Class method as a constructor 
emp_str_1 = 'John-Doe-70000' 
emp_str_2 = 'Jane-Doe-50000'    
emp_str_3 = 'John-Smith-40000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)




Employee.set_raise_amount(1.05)


""" print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount) """
