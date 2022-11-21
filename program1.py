# Write a recursive python function to print first N natural numbers.

def Netural(n):
  if n==1:
    print(1)
  else:
    print(n)  
    Netural(n-1)

Netural(3)  