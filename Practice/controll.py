# If statement

print("If statement")
score = int(input("Enter score: "))

if score >= 90:
    print("You got grade A")
elif score >= 80:
    print("You got grade B")
elif score >=70:
    print("You got grade C")
elif score >= 60:
    print("You got grade D")
elif score >= 50:
    print("You got grad E")
else:
    print("You got grade F")

    
# Match statement
day = int(input("Enter number of day:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: 
        print("Number not invalid")