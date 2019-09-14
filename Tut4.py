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


    @classmethod # Normal class 
    def set_pay_raise(cls, value):
        cls.pay_raise = value


    @classmethod # Acts as an alternative constructor when each instance is set up 
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, float(pay))


    @staticmethod # Give away: you don't need to access the cls or self variable 
    def is_workday(day):
        return day.weekday == 5  or day.weekday == 6 

#===============================================================================
# Inheritance 

class Developer(Employee):
    pay_raise = 1.1

    def __init__(self, First, Last, pay, prog_lang):
        super().__init__(First, Last, pay)
        #Employee.__init__(self, First, Last, pay)
        self.prog_lang = prog_lang
    


dev_1 = Developer('Corey', 'Schaffer', 50000, 'Python')
dev_2 = Developer('John', 'Smith', 60000, 'Java')

"""print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)"""


#print(dev_1.email)
#print(dev_1.prog_lang)


#===============================================================================
# Inheritance 
class Manager(Employee):

    def __init__(self, First, Last, pay, employees = None):
        super().__init__(First, Last, pay)
        if employees is None: 
            self.employees = []
        else: 
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


mgr1 = Manager('Sue', 'Smith', 9000, [dev_1])


#mgr1.add_emp(dev_2)
#print(mgr1.email)
#mgr1.print_emps()



print(isinstance(mgr1, Developer))
print(issubclass(Developer, Employee))