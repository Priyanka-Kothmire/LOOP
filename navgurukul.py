i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul",i)
    elif i%3==0:
        print("nav:",i)
    elif i%7==0:
        print("gurukul:",i)
    else:
        print("others numbers;",i)
    i=i+1 