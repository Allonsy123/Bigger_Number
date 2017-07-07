no1 = input("Pick a number")
no2 = input("Pick another number")

def Bigger():
    if no1 > no2:
        print("Your first number", no1, "is larger than your second number.", no2)
    elif no2 > no1:
        print("Your second number", no2, "is larger than your first number.", no1)
    else:
        print("Your numbers have the same value, and therefore one is not bigger than the other.")

Bigger()
