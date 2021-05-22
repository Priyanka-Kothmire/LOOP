i=int(input("enter the number :"))
sum=0
orig=i
while (i>0):
    sum=sum+(i%10)*(i%10)*(i*10)
    i=i//10
if orig==sum:
    print("this is armstrong number")
else:
    print("this is not armstrong number")
