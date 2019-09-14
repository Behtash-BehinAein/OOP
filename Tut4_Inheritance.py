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


# ======================================================================================================================



print(mgr_1.email)
#mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()



#print(help(Developer))
""" 
print(dev_1.email)
print(dev_1.prog_lang)
 """