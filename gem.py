print("Welcome to my shop")
print("please order something below")
#creating a dict
menu = {
    "Tea" : 10,
    "Coffee" : 5,
    "Juice" : 7,
    }
# Showing menu
for item,price in menu.items():
    print("- {}: ${}".format(item, price))
#choosing
choose=input("what do you want ?. type here:").capitalize()
if choose in menu :
    print ("order sucessfull!")
    print ("Visit again, Thank You")
else :
    # everyone orders one so,
    print("only choose the items in the menu")
