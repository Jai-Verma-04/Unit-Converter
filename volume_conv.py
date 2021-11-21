from time import sleep

def run():
    running = True
    while running:
        choice1 = ask_choice1() 
        choice2 = ask_choice2()

        if choice1==1:
            if choice2==1:
                print("Can't convert, Same units entered!!!")
                sleep(1)
                break

            elif choice2==2:
                try:
                    value_lm = float(input("Enter the Volume in Litres: "))
                    ans = round(l_to_ml(value_lm), 2)
                    print(f"{value_lm} L = {ans} mL")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            elif choice2==3:
                try:
                    value_lo = float(input("Enter the Volume in Litres: "))
                    ans = round(l_to_ounce(value_lo), 2)
                    print(f"{value_lo} L = {ans} Fluid ounce")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            else:
                print("Choice 2 was correct..Start Over!!")
                sleep(1)
                run()

        elif choice1==2:
            if choice2==1:
                try:
                    value_m_l = float(input("Enter the volume in mL: "))
                    ans = round(ml_to_L(value_m_l),2)
                    print(f"{value_m_l} mL = {ans} Litres")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            elif choice2==2:
                print("Can't convert, Same units entered!!!")
                sleep(1)
                break

            elif choice2==3:
                try:
                    value_mo = float(input("Enter the volume in mL: "))
                    ans = round(ml_to_o(value_mo),2)
                    print(f"{value_mo} mL = {ans} Fluid ounce")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()
                
            else:
                print("Choice 2 was Incorrect..Start Over!!")
                sleep(1)
                run()
        
        elif choice1==3:
            if choice2==1:
                try:
                    value_ol = float(input("Enter the volume in fluid ounce: "))
                    ans = round(o_to_l(value_ol),2)
                    print(f"{value_ol} fluid ounce = {ans} Liters")
                    sleep(1)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()
               
            elif choice2==2:
                try:
                    value_om = float(input("Enter the volume in fluid ounce: "))
                    ans = round(o_to_ml(value_om),2)
                    print(f"{value_om} fluid ounce = {ans} mL")
                    sleep(1)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    run()
            
            elif choice2==3:
                print("Can't convert, Same units entered!!!")
                sleep(1)
                break
            else:
                print("Choice 2 was Incorrect..Start Over!!")
                sleep(1)
                run()
        else:
            print("Some error in program..")
            print("Trying to resolve the problem...")
            sleep(4)
            print("Couldn't resolve problem..\nExiting in")
            print(3);sleep(1);print(2);sleep(1);print(1)
            break


def l_to_ml(value):
    ans = value*1000
    return ans

def l_to_ounce(value):
    ans = value*35.195
    return ans

def ml_to_L(value):
    ans = value/1000
    return ans

def ml_to_o(value):
    ans = value/28.413
    return ans

def o_to_l(value):
    ans = value/35.195
    return ans

def o_to_ml(value):
    ans = value*28.413
    return ans

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

