n = int(input("Enter a number uptill you want to have fibonacci series:"))
x = 0
y = 1
if n<=0:
    print("please enter positive number")
elif n==1:
    print("Fibonacci series is as follows:")
    print(x)
else:
    print("Fibonacci series is as follows:")
    print(x , y,end=" ")
    for i in range(2,n):
        z = x+y
        print(z,end=" ")
        x = y
        y = z
