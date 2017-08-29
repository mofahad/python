class Employee:

   raise_amount = 1.04
   def __init__(self,first,last,pay):
     self.first = first
     self.last = last
     self.pay = pay
     self.email = first+"."+last+"@company.com"
   
   def fullname(self): 
     return '{} {}'.format(self.first,self.last) 
   
   
   def raise_amount(self):
     self.pay = int(self.pay*raise_amount)  
     
emp1 = Employee("fahad","mushahid",230000)
emp2 = Employee("rahul","tenda",121331)
 
print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp1.pay)
emp1.raise_amount()
print(emp1.pay)

