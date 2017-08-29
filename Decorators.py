def outer_fun(x):
  def inner_fun(y):
     return  x+y
  return inner_fun

outer_fun(2)(44)   
outer_fun()
