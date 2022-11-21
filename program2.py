# Write a recursive python function to print first N natural numbers in reverse order


def f(n):
  if n==1:
    return 1
  print(n)  
  return (f(n-1))

print(f(4))   
