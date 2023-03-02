fare = float(input("Enter your fare: "))

print("Codes "
      "\nO - ORDINARY"
      "\nS - STUDENT"
      "\nC - SENIOR CITIZEN"
      "\nReminder: Should be in capital letter")
CosCode = input("Enter a code: ")

if CosCode == "C":
    netFare = fare - ((fare / 100) * 20)
    print("You are a Senior Citizen")
    print("Your discount rate is 20%")
    print("Your total net fare is: " + str(netFare))

elif CosCode == "S":
    netFare = fare - ((fare / 100) * 10)
    print("You are a Student")
    print("Your discount rate is 10%")
    print("Your total net fare is: " + str(netFare))

elif CosCode == "O":
    print("You are an Ordinary Costumer")
    print("You don't have any discount")
    print("Your net fare is: " + str(fare))

else:
    print("Invalid Code: Error")