from sys import exit

def fibonacci(n):

 if n==0:
  return 1
 elif n==1:
  return 1
 elif n>2:
  return fibonacci(n-1)+fibonacci(n-2)
  
for n in range(1,701):
 print(n,":",fibonacci(n))
exit(0)

