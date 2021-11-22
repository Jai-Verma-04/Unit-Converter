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
                    value_km_m = float(input("Enter the Length in Kilometer: "))
                    ans = round(km_m(value_km_m), 2)
                    print(f"{value_km_m} Km = {ans} m")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            elif choice2==3:
                try:
                    value_km_mi = float(input("Enter the Length in Kilometer: "))
                    ans = round(km_mi(value_km_mi), 2)
                    print(f"{value_km_mi} Km = {ans} mi")
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
                    value_m_km = float(input("Enter the Length in meter: "))
                    ans = round(m_km(value_m_km),2)
                    print(f"{value_m_km} m = {ans} Km")
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
                    value_m_mi = float(input("Enter the Length in meter: "))
                    ans = round(m_mi(value_m_mi),2)
                    print(f"{value_m_mi} m = {ans} mi")
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
                    value_mi_km = float(input("Enter the Length in Mile: "))
                    ans = round(mi_km(value_mi_km),2)
                    print(f"{value_mi_km} mi = {ans} Km")
                    sleep(1)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()
               
            elif choice2==2:
                try:
                    value_mi_m = float(input("Enter the Length in Mile: "))
                    ans = round(mi_m(value_mi_m),2)
                    print(f"{value_mi_m} mile = {ans} meter")
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

def km_m(value):
    ans = value*1000
    return ans

def km_mi(value):
    ans = value/1.609
    return ans

def m_km(value):
    ans = value/1000
    return ans

def m_mi(value):
    ans = value/1609
    return ans

def mi_km(value):
    ans = value*1.609
    return ans

def mi_m(value):
    ans = value*1609
    return ans
    
def ask_choice1():
    print("\nChoose from which unit you want to convert from: ");sleep(0.5)
    print("1. Kilometers")
    print("2. Meter")
    print("3. Mile\n");sleep(0.5)
    
    try:
        choice1 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice1()
    return choice1


def ask_choice2():
    print("Choose which unit you want to convert to: ");sleep(0.5)
    print("1. Kilometer")
    print("2. Meter")
    print("3. Mile\n");sleep(0.5)

    try:
        choice2 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice2()
    return choice2

