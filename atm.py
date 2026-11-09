pin=1234
bal=1500
pas = int(input("Enter your pin:"))
if pas != pin:
    print("wrong pin")
elif pas==pin:
    h = int(input ("choose option 1 or 2:"))
    if h == 1:
        print("Balance:${}".format(bal))
    elif h == 2:
        g=int(input("How many dollor(s) you want:"))
        if g < 1500 :
            m = bal-g
            print ("Your balance is :${}".format(m))
        elif g > 1500 :
            print ("Enter an amount that is less than to your balance amount")
    elif h != 1 or 2 :
        print ("enter 1 or 2")