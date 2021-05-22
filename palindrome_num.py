i=int(input("enter the number"))
original=i
rev=0
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if original==rev:
    print("it is palindrome")
else:
    print("not palindrome")

