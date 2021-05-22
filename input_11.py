i=1
sum=0
while i<=11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    print(sum)
    i=i+1
print("Average of weight",sum/11)
if (sum/11)%5==0 :
    print("it is multiple by 5")
else:
    print("its not a multiple by 5")

    
    

   
