# function
def menu():
    print ("1) Sum")
    print ("2) substract")
    print ("3) multiply")
    print ("4) divide")
    
# call the function
menu()
# read the input of the keyboard
opt = input("Select and option")
# try to continue with the calculator app 
num1 = int(input("Please enter a number "))
num2 = int(input("Please enter another number "))

if opt == "1":
    total = num1 + num2
    print ("The total is " + str(total))
elif opt == "2":
    total = num1 - num2
    print ("The total is " + str(total))
elif opt == "3":
    total = num1 * num2
    print ("The total is " + str(total))
elif opt == "4":
    if num2 == 0:
        print("you cannot divide by zero")
    else:
        total = num1 / num2
        print("The total is " + str(total))
else: 
    print("thats not a valid option")