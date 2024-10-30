print("---------- Mini calculator----------")

num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

print("Press 1 for addition\nPress 2 for substraction\nPress 3 for multiplication\nPress 4 for division")
choice = int(input("Enter your choice :"))
if choice == 1:
    print(f"Sum of num1 and num2 is {num1 + num2 }")

elif choice == 2:
    print(f"Substraction of num1 and num2 is {num1 - num2}")

elif choice == 3:
    print (f"Multiplication of num1 and num2 is {num1*num2}")

elif choice == 4:
    print (f"Division of num1 from num2 is {num1/num2} ")

else:
    print("Please choose the valid option")