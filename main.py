"""1.1 implement program using recursion to find a factorial of a number """
def fact(n):
  if (n<=1):
    return 1
  else:
    return(n*fact(n-1))

num=int(input("enter a number:"))
result=fact(num)
print("factorial of",num,"is",result)