#Input username and password

user_name = input("Enter your name: ")
password = input("Enter your password: ")

if user_name == "admin" and password == "admin123":
    print("Access granted")
else:
    print("Access denied")
