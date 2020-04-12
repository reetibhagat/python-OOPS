class Employee:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)




emp_1 = Employee('Reeti', 'Bhagat', 33)
emp_4 = Employee('Ajesh', 'Mahto', 35)

print(emp_1.fullname())
print(Employee.fullname(emp_1))