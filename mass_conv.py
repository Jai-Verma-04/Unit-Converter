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
                    value_kg_g = float(input("Enter the Mass in Kgs: "))
                    ans = round(kg_g(value_kg_g), 2)
                    print(f"{value_kg_g} Kg = {ans} g")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            elif choice2==3:
                try:
                    value_kg_p = float(input("Enter the Mass in Kgs: "))
                    ans = round(kg_lb(value_kg_p), 2)
                    print(f"{value_kg_p} Kg = {ans} lb")
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
                    value_g_kg = float(input("Enter the mass in grams: "))
                    ans = round(g_kg(value_g_kg),2)
                    print(f"{value_g_kg} g = {ans}Kg")
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
                    value_g_p = float(input("Enter the mass in grams: "))
                    ans = round(g_lb(value_g_p),2)
                    print(f"{value_g_p} g = {ans} lb")
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
                    value_p_kg = float(input("Enter the Mass in Pounds: "))
                    ans = round(lb_kg(value_p_kg),2)
                    print(f"{value_p_kg} lb = {ans} Kg")
                    sleep(1)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()
               
            elif choice2==2:
                try:
                    value_p_g = float(input("Enter the Mass in Pounds: "))
                    ans = round(lb_g(value_p_g),2)
                    print(f"{value_p_g} pounds = {ans} g")
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


def kg_g(value):
    ans = value*100
    return ans

def kg_lb(value):
    ans = value*2.205
    return ans

def g_kg(value):
    ans = value/1000
    return ans

def g_lb(value):
    ans = value/454
    return ans

def lb_kg(value):
    ans = value/2.205
    return ans

def lb_g(value):
    ans = value*454
    return ans

def ask_choice1():
    print("\nChoose from which unit you want to convert from: ");sleep(0.5)
    print("1. Kilogram")
    print("2. Gram")
    print("3. Pound\n");sleep(0.5)
    
    try:
        choice1 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice1()
    return choice1


def ask_choice2():
    print("Choose which unit you want to convert to: ");sleep(0.5)
    print("1. Kilogram")
    print("2. Gram")
    print("3. Pound\n");sleep(0.5)

    try:
        choice2 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice2()
    return choice2

