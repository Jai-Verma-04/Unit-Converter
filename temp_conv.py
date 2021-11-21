from time import sleep
from math import sqrt
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
                    value_cf = float(input("Enter the temperature in °C: "))
                    ans = round(c_to_f(value_cf), 2)
                    print(f"{value_cf}°C = {ans}°F")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            elif choice2==3:
                try:
                    value_ck = float(input("Enter the temperature in °C: "))
                    ans = round(c_to_k(value_ck), 2)
                    print(f"{value_ck}°C = {ans} Kelvin")
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
                    value_fc = float(input("Enter the temperature in °F: "))
                    ans = round(f_to_c(value_fc),2)
                    print(f"{value_fc}°F = {ans}°C")
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
                    value_fk = float(input("Enter the temperature in °F: "))
                    ans = round(f_to_k(value_fk),2)
                    print(f"{value_fk}°F = {ans} Kelvin")
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
                    value_kc = float(input("Enter the temperature in Kelvin: "))
                    ans = round(k_to_c(value_kc),2)
                    print(f"{value_kc} Kelvin = {ans} °C")
                    sleep(1)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()
               
            elif choice2==2:
                try:
                    value_kf = float(input("Enter the temperature in Kelvin: "))
                    ans = round(k_to_f(value_kf),2)
                    print(f"{value_kf} Kelvin = {ans}°F")
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


def ask_choice1():
    print("\nChoose from which unit you want to convert from: ");sleep(0.5)
    print("1. °C")
    print("2. °F")
    print("3. Kelvin\n");sleep(0.5)
    
    try:
        choice1 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice1()
    return choice1


def ask_choice2():
    print("Choose which unit you want to convert to: ");sleep(0.5)
    print("1. °C")
    print("2. °F")
    print("3. Kelvin\n");sleep(0.5)

    try:
        choice2 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice2()
    return choice2


def c_to_f(value):
    value_f = (value*9/5) + 32
    return value_f


def c_to_k(value):
    value_k = value + 273.15 
    return value_k


def f_to_c(value):
    value_c = (value-32)*5/9
    return value_c


def f_to_k(value):
    value_k = (value-32)*5/9 + 273.15
    return value_k


def k_to_c(value):
    value_c = value-273.15
    return value_c


def k_to_f(value):
    value_f = (value-273.15)*9/5 + 32
    return value_f
