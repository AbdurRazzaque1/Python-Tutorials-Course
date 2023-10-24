print("Press 1 to park Or press -1 to remove a Riksha. \nPress 2 to park Or press -2 to remove a Car. \nPress 3 to park Or press -3 to remove a Bus. \nPress 4 to erase all the data. \nPress 5 to see record. \npress 0 to quit the program.")
c = 0
d = 0
e = 0
f = 0
a = 0
while (True):
    b = int(input("Press your choise: "))
    if (-3 <= b <= 5 and b != 0):
        if (c < 50):
            if (b == 1):
                a += 100
                d += 1
            elif (b == -1):
                if (d > 0):
                    d -= 1
                else:
                    print("Sorry, No Rikshaw is present in the parking")
            elif (b == 2):
                a += 200
                e += 1
            elif (b == -2):
                if (e > 0):
                    e -= 1
                else:
                    print("Sorry, No Car is present in the parking")
            elif (b == 3):
                a += 300
                f += 1
            elif (b == -3):
                if (f > 0):
                    f -= 1
                else:
                    print("Sorry, No Bus is present in the parking")
            elif (b == 4):
                a = 0
                c = 0
                d = 0
                e = 0
                f = 0
            elif (b == 5):
                print(f"The number of Rikshaws is {d}")
                print(f"The number of Cars is {e}")
                print(f"The number of Buses is {f}")
                print(f"The tatal number of vehical in the parking is {c} and total amount is ₹{a}")
        elif (b == 4):
            a = 0
            c = 0
            d = 0
            e = 0
            f = 0
        elif (b == 5):
            print(f"The number of Rikshaws is {d}")
            print(f"The number of Cars is {e}")
            print(f"The number of Busses is {f}")
            print(f"The tatal number of vehical in the parking is {c} and total amount is ₹{a}")
        else:
            print("Sorry the parking is full. Remove a vehicle from the parking and then park a new vehicle.")
    elif (b == 0):
        print("THANK YOU SO MUCH FOR USING THIS PROGRAM")
        break
    else:
        print("Something went wrong")
    c = d + e + f