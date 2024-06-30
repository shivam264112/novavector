print ("calculator ")
num1 = float(input("enter first number here : "))
num2 = float(input ("enter second number here :"))

print ("press 1 for addition endl")
print("press 2 for substraction endl")
print("press 3 for multiplication endl")
print("press 4 for division endl")
choice = int(input("enter your choice from 1-4: "))
if choice == 1 :
    print ("The addition of given two number is",num1 + num2)
elif choice ==2 :
     print ("The substraction  of given two number is",num1 - num2)
elif choice == 3 :
      print ("The multiplication  of given two number is",num1 * num2)
elif choice == 4 :
      print ("The division  of given two number is",num1 / num2)
else :
     print("invalid input")

