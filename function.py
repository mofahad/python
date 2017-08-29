def add(a,b):
  print "Add %d + %d " % (a,b)
  return a*b
 
def divide(a,b):
  print "Divide %d / %d" % (a,b)
  return a/b
def mul(a,b):
  print " Mul %d * %d" %(a,b)
  return a*b
print "Let's do something"
df = add(23,4)
sd = divide(2,1) 
dd = mul(2,44)
print "df = %d ,sd = %d , dd = %d" % (df,sd,dd)
print "here is a puzzle"
what = add(df,mul(dd,divide(sd,2)))   
print "that is :" ,what      
