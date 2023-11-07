"Vehical Parking Problem"

print("Press 1 to park Or press -1 to remove a Riksha.")
print("Press 2 to park Or press -2 to remove a Car.")
print("Press 3 to park Or press -3 to remove a Bus.")
print("Press 4 to erase all the data.")
print("Press 5 to see record.")
print("press 0 to quit the program.\n")
C = 0
D = 0
E = 0
F = 0
A = 0
while True:
    B = int(input("Press your choise: "))
    if (-3 <= B <= 5 and B != 0):
        if C < 50:
            if B == 1:
                A += 100
                D += 1
            elif B == -1:
                if D > 0:
                    D -= 1
                else:
                    print("Sorry, No Rikshaw is present in the parking")
            elif B == 2:
                A += 200
                E += 1
            elif B == -2:
                if E > 0:
                    E -= 1
                else:
                    print("Sorry, No Car is present in the parking")
            elif B == 3:
                A += 300
                F += 1
            elif B == -3:
                if F > 0:
                    F -= 1
                else:
                    print("Sorry, No Bus is present in the parking")
                    
            elif B == 4:
                A = 0
                C = 0
                D = 0
                E = 0
                F = 0
            elif B == 5:
                print(f"The number of Rikshaws is {D}")
                print(f"The number of Cars is {E}")
                print(f"The number of Buses is {F}")
                print(f"The tatal number of vehical in the parking is {C} and total amount is ₹{A}")
        elif B == 4:
            A = 0
            C = 0
            D = 0
            E = 0
            F = 0
        elif B == 5:
            print(f"The number of Rikshaws is {D}")
            print(f"The number of Cars is {E}")
            print(f"The number of Busses is {F}")
            print(f"The tatal number of vehical in the parking is {C} and total amount is ₹{A}")
        else:
            print("Sorry the parking is full.", end= " ")
            print("Remove a vehicle from the parking and then park a new vehicle.")
    elif B == 0:
        print("THANK YOU SO MUCH FOR USING THIS PROGRAM")
        break
    else:
        print("Something went wrong")
    C = D + E + F
