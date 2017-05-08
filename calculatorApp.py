from calculator import Calculator

print "Welcome to the Calculator Programme."
print '' 
print "Please select from one of the options below:"
print "Enter 1 for addition."
print "Enter 2 for subtraction."
print "Enter 3 for multiplication."
print "Enter 4 for division."
print "Enter 5 for square."
print "Enter 6 to cube."
print "Enter 7 for exponentiation."
print "Enter 8 to get the Square Root."
print "Enter 9 to use pi."
print "Enter 10 to generate the factorial."
print ''
print "Enter 0 to leave the programme."


if __name__=='__main__':
    while True:
        choice = input("Enter your choice now: ")
        if choice > 0 and choice < 11:
            a = input('Please enter a number: ')
            if choice == 1:
                b = input('Please type second number to add: ')
                x = input('Please enter a range: ')
                print(Calculator(a, b).add())
            elif choice == 2:
                b = input('Please type second number to subtract: ')
                print (Calculator(a, b).subtract())
            elif choice == 3:
                b = input('Please type second number to multiply: ')
                print (Calculator(a, b).multiply()) 
            elif choice == 4:
                b = input('Please type second number to divide: ')
                print (Calculator(a, b).divide())
            elif choice == 5:
                print (Calculator(a, b).square()) 
            elif choice == 6:
                print (Calculator(a, b).cube()) 
            elif choice == 7:
                b = input('What value would you like to exponentiate to the value of: ')
                print (Calculator(a, b).expon())
            elif choice == 8:
                print (Calculator(a, b).sqrt())
            elif choice == 9:
                print (Calculator(a, b).pi())
            elif choice == 10:
                print (Calculator(a, b=0).factorial()) 
            else: 
                print "Error."
        elif choice == 0:
            break
        else:
            print ("Error please make a valid selection between 1 and 10.")
