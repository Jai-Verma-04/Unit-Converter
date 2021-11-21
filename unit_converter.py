from time import sleep
import temp_conv
import volume_conv

running=True
while running:
    try:
        print("\nWelcome to Converter Program!!!"); sleep(0.5)
        print('1. Temperature converter..')
        print('2. Volume converter..')
        print('3. Mass converter..')
        print('4. Length Converter..')
        print('5. Digital Storage Converter..\n');sleep(0.5)
        print('NOTE: If wrong values are supplied at conversion window, the program will start over\
and user would need to re-enter all the values that were entered before.. Be careful!')
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            temp_conv.run() 
        elif choice == 2:
            volume_conv.run()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            print("Invalid choice Entered..Try Again");sleep(1)
            continue
    except:
        print("Please enter only a number..try again");sleep(1)
        continue
    
    try:
        again = input("Do you want to run the program again??[y/n] >>").lower()
        
        if again == 'y':
            continue
        elif again == 'n':
            running = False
        else:
            print("You seem to have entered inorrect choice..")
            print("We'll run the program again for you :)");sleep(2)
    except:
        print("Enter correct values!")
        continue
