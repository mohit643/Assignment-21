# Write a recursive python function to print first N odd natural numbers

def f(n):
  if n==1:
    print(1)
  else:
    print(2*n-1)
    f(n-1)  
  
    


f(3) 