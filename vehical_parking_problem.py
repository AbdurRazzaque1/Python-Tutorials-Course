"Vehical Parking Problem"

print("Press 1 to park Or press -1 to remove a Rikshaw.")
print("Press 2 to park Or press -2 to remove a Car.")
print("Press 3 to park Or press -3 to remove a Bus.")
print("Press 4 to erase all the data.")
print("Press 5 to see record.")
print("press 0 to quit the program.\n")
totalVehicles = 0
rikshaws = 0
cars = 0
buses = 0
totalAmount = 0
while True:
    choice = int(input("Press your choise: "))
    if (-3 <= choice <= 5 and choice != 0):
        if totalVehicles < 50:
            if choice == 1:
                totalAmount += 100
                rikshaws += 1
            elif choice == -1:
                if rikshaws > 0:
                    rikshaws -= 1
                else:
                    print("\n*** Sorry, No Rikshaw is present in the parking ***\n")
            elif choice == 2:
                totalAmount += 200
                cars += 1
            elif choice == -2:
                if cars > 0:
                    cars -= 1
                else:
                    print("\n*** Sorry, No Car is present in the parking ***\n")
            elif choice == 3:
                totalAmount += 300
                buses += 1
            elif choice == -3:
                if buses > 0:
                    buses -= 1
                else:
                    print("\n*** Sorry, No Bus is present in the parking ***\n")
                    
            elif choice == 4:
                print("\n#! All the data has been removed from the parking record !#\n")
                totalAmount = 0
                totalVehicles = 0
                rikshaws = 0
                cars = 0
                buses = 0
            elif choice == 5:
                print("\n#!**************************!#")
                print(f"The number of Rikshaws is {rikshaws}")
                print(f"The number of Cars is {cars}")
                print(f"The number of Buses is {buses}")
                print(f"The tatal number of vehical in the parking is {totalVehicles} and total amount is ₹{totalAmount}")
                print("#!**************************!#\n")
        elif choice == 4:

            print("\n#! All the data has been removed from the parking record !#\n")
            totalAmount = 0
            totalVehicles = 0
            rikshaws = 0
            cars = 0
            buses = 0
        elif choice == 5:
            print("\n#!**************************!#")
            print(f"The number of Rikshaws is {rikshaws}")
            print(f"The number of Cars is {cars}")
            print(f"The number of Busses is {buses}")
            print(f"The tatal number of vehical in the parking is {totalVehicles} and total amount is ₹{totalAmount}")
            print("#!**************************!#\n")
        else:
            print("\n#? Sorry the parking is full,", end= " ")
            print("Remove a vehicle OR Erase all the data to park new vehicles #?.\n")
    elif choice == 0:
        print("\n*** THANK YOU SO MUCH FOR USING THIS PROGRAM ***\n")
        break
    else:
        print("\n#!!!! Something went wrong !!!!#\n")
    totalVehicles = rikshaws + cars + buses
