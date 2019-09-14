import os
clear = lambda: os.system('cls')
clear()

class Employee():

    pay_raise   = 1.05  # Class variable   | will be set via instances 
    num_emp     = 0     # Class variable   | will be set via the class

    def __init__(self, First, Last, pay):  # Istance variables 
        self.First = First
        self.Last  = Last
        self.email = First + '.' + Last + '@company.com'
        self.pay   = pay
        Employee.num_emp  += 1 

    def fullname(self):
        return f'{self.First } {self.Last}'

    def apply_raise(self):
         self.pay = int(self.pay_raise * self.pay)


    @classmethod # 
    def set_pay_raise(cls, value):
        cls.pay_raise = value


    @classmethod # Acts as an alternative constructor when each instance is set up 
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, float(pay))


    @staticmethod # Give away: you don't need to access the cls or self variable 
    def is_workday(day):
        return day.weekday == 5  or day.weekday == 6 


import datetime 
my_date = datetime.date(2018,12,8)
print(Employee.is_workday(my_date))



Employee.set_pay_raise(1.1)

emp1_string = 'Corey-Schaffer-60000'
emp1 = Employee.from_string(emp1_string)
#emp1 = Employee('Corey', 'Schaffer', 60000) 

emp2 = Employee('Don', 'Johnson', 50000) 

print(emp1.pay)
print('--'*10)
Employee.apply_raise(emp1)
Employee.apply_raise(emp2)

print(emp1.pay)
print(emp2.pay)
print(Employee.num_emp)

print('--'*10)

