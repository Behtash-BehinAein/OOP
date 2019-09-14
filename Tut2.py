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
        Employee.num_emp   += 1 

    def fullname(self):
        return f'{self.First } {self.Last}'

    def apply_raise_ind(self):
         self.pay = int(self.pay_raise * self.pay)



emp1 = Employee('Corey', 'Schaffer', 60000) 
emp2 = Employee('Don', 'Johnson', 50000) 

print(emp1.pay)
print('--'*10)
Employee.apply_raise_ind(emp1)
print(emp1.pay)
print(emp2.pay)
print(Employee.num_emp)
