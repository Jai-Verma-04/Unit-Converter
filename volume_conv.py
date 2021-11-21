from time import sleep

def run():
    running = True
    while running:
        choice1 = ask_choice1() 
        choice2 = ask_choice2()




def ask_choice1():
    print("\nChoose from which unit you want to convert from: ");sleep(0.5)
    print("1. Liter")
    print("2. Milliliter")
    print("3. Fluid Ounce\n");sleep(0.5)
    
    try:
        choice1 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice1()
    return choice1


def ask_choice2():
    print("Choose which unit you want to convert to: ");sleep(0.5)
    print("1. Liter")
    print("2. Milliliter")
    print("3. Fluid ounce\n");sleep(0.5)

    try:
        choice2 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice2()
    return choice2

