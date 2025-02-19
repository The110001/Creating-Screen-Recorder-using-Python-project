# practice 8
# let the user provide 5 numbers. Then choose the mathematical operation to be operated on the values chosen by the user themselves.

# all the beforehand functions and loops and conditions
# the list function
def list():
    n = 1
    mylist = []

    print("let us create the list first.")
    print("")
    while n <= 5 :
        value = input("** please provide a number here: ")
        if value.isdigit():
            mylist.append(value)
            n += 1
        else:
            print("")
            print("the input provided is not a number.\n"
                  "please try again.")
    return mylist

# the program function
def program():
    operations = ["a", "b", "c", "d", "e"]
    print("please choose a mathematical operation from the below options:\n"
          "a/ addition\n"
          "b/ subtraction\n"
          "c/ division\n"
          "d/ multiplication\n"
          "e/ exponents")
    print("")
    # event loop
    while True:
        choice = input("** please type the alphabet associated with your chosen operation.\n"
                       "your options are a, b, c, d and e.\n"
                       "--> ")
        if choice in operations:
            # choice a
            if choice == "a":
                num1 = input("** now please choose one number from the list you created: ")
                num2 = input("** now please choose another number from the list you created: ")
                if (num1.isdigit() and num2.isdigit()) and (num1 in result and num2 in result):
                    addition = int(num1) + int(num2)
                    return f"the addition of the two numbers is: {addition}"
                else:
                    print("")
                    print("your input is not valid.\n"
                          "please try again.")
            # choice b
            elif choice == "b":
                num1 = input("** now please choose one number from the list you created: ")
                num2 = input("** now please choose another number from the list you created: ")
                if (num1.isdigit() and num2.isdigit()) and (num1 in result and num2 in result):
                    subtraction = int(num1) - int(num2)
                    return f"the subtraction of the two numbers is: {subtraction}"
                else:
                    print("")
                    print("your input is not valid.\n"
                          "please try again.")
            # choice c
            elif choice == "c":
                num1 = input("** now please choose one number from the list you created: ")
                num2 = input("** now please choose another number from the list you created: ")
                if (num1.isdigit() and num2.isdigit()) and (num1 in result and num2 in result):
                    division = int(num1) / int(num2)
                    return f"the division of the two numbers is: {division}"
                else:
                    print("")
                    print("your input is not valid.\n"
                          "please try again.")
            # choice d
            elif choice == "d":
                num1 = input("** now please choose one number from the list you created: ")
                num2 = input("** now please choose another number from the list you created: ")
                if (num1.isdigit() and num2.isdigit()) and (num1 in result and num2 in result):
                    multiplication = int(num1) * int(num2)
                    return f"the multiplication of the two numbers is: {multiplication}"
                else:
                    print("")
                    print("your input is not valid.\n"
                          "please try again.")
            # choice e
            elif choice == "e":
                num1 = input("** now please choose one number from the list you created: ")
                num2 = input("** now please choose another number from the list you created: ")
                if (num1.isdigit() and num2.isdigit()) and (num1 in result and num2 in result):
                    exponent = int(num1) ** int(num2)
                    return f"the exponent of {num1} by {num2} is: {exponent}"
                else:
                    print("")
                    print("your input is not valid.\n"
                          "please try again.")
        else:
            print("")
            print("your input is not valid.\n"
                  "please try again.")
            print("")


# where the event begins
print("hello there. in order to make our program work, we need you to first create a list of numbers.\n"
      "then you will be given a bunch of mathematical operation options and it is you that will decide\n"
      "which one to be used. then we will do the rest of the process for you.\n"
      "READY, GO :)")
print("")

result = list()
print("")
print(f"this is the final list: {result}")
print("")

result = program()
print(result)