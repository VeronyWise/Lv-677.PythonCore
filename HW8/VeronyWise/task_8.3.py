class Employee():
     counter = 0
     def __init__(self, name, salary):
         self.name = name
         self.salary = salary
         Employee.counter += 1
     
     @classmethod
     def total_number(cls):
          print(f'Total number of employees is {cls.counter}')
          
     def info_employee(self):
          print(f'The salary {self.salary} $ is for {self.name} ')

employee_1 = Employee("Alfredo", 1250)
employee_2 = Employee("Javelina", 1350)

employee_1.info_employee()
employee_2.info_employee()
Employee.total_number()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
