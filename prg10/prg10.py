print("enter 3 numbers")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
     print("larger number is",a)
elif b>a and b>c:
     print("larger number is",b)
else:
     print("larger number is",c)