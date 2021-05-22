i=int(input("enter the number :"))
sum=0
product=1
while i>0:
    d=i%10
    if d%2==0:
    
        sum=sum+d
    else:
        product=product*d
    i=i//10
print("sum of digit=",sum, "product of digit=",product)
print(sum)
