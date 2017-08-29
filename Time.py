import tensorflow as tf
import time

n=10000
start_time = time.time()
L =[]
for i in range(n):
  L = L +[i*2]
print(time.time()-start_time )

start_time = time.time()
L= []
for i in range(n):
  L = L+[i*2] 
  print(time.time()-start_time)   
