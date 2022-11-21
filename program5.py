# Write a recursive python function to print first N even natural numbers.


def f(n):
  
  if n>1:
    print(n)
    f(n-1)
  else:
    print(1)


f(3)