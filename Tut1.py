import os
clear = lambda: os.system('cls')
clear()

class Employee():

    def __init__(self, First, Last, pay):  # Istance variables 
        self.First = First
        self.Last  = Last
        self.email = First + '.' + Last + '@company.com'
        self.pay   = pay 

    def fullname(self):
        return f'{self.First } {self.Last}'



emp1 = Employee('Corey', 'Schaffer', 60000) 
print(emp1.fullname())
print('--'*10)
print(Employee.fullname(emp1))