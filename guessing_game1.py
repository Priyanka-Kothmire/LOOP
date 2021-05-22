i=1
n=7
while i<=10:
    guess=int(input("enter the guessing number"))
    if guess>=7:
        print("greter")
        break
    else:
        print("less")
        i=i+1