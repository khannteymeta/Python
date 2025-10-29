#Arithmetic operators
num1,num2=map(int,input("Enter 2 numbers: ").split())
print(f"The sum is: {num1+num2}")
print(f"\nThe subtraction is: {num1-num2}")
print(f"\nThe multiplication is: {num1*num2}")
print(f"\nThe division is: {float(num1/num2):.2f}")
print(f"\nThe floor division is: {num1//num2}")
print(f"\nThe modulus is: {num1%num2}")
print(f"\nThe Exponentiation is: {num1**num2}")
print(f"\n---------------------------------------------")

#Comparison operators
print("Comparison operators")
print(f"\nValue1 == value2: {num1==num2}")
print(f"\nValue1 != value2: {num1!=num2}")
print(f"\nValue1 > value2: {num1>num2}")
print(f"\nValue1 < value2: {num1<num2}")
print(f"\nValue1 >= value2: {num1>=num2}")
print(f"\nValue1 <= value2: {num1<=num2}")
print(f"\n---------------------------------------------")

#Logical operators
print("Logical operators")
print(f"\nValue1 > 50 and value2 < 100: {num1>50 and num2<100}")
print(f"\nValue1 > 50 or value2 < 100: {num1>50 or num2<100}")
print(f"\nValue1 > 50 or value2 < 100: {not(num1>50 or num2<100)}")
print(f"\n---------------------------------------------")

#Membership operators

fruit=["Orange","Grape","Apple"]
print("Membership operators")
print(f"\nIs mango in the list? {"Mango" in fruit}, \nIs apple in the list? {"Apple" in fruit}")
print(f"\n---------------------------------------------")

#Identity operator
a=[1,3];b=a;c=[1,3]
print("Identity operators")
print(f"\nTrue (same object in memory): {a is b}")
print(f"\nFalse (same value, but different objects): {a is c}")
print(f"\n---------------------------------------------")