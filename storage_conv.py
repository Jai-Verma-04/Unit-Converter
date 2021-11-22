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
                    value_kb_mb = float(input("Enter the storage in Kilobyte: "))
                    ans = round(kb_mb(value_kb_mb), 2)
                    print(f"{value_kb_mb} Kb = {ans} Mb")
                    sleep(2)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()

            elif choice2==3:
                try:
                    value_kb_gb = float(input("Enter the storage in Kilobyte: "))
                    ans = round(kb_gb(value_kb_gb), 2)
                    print(f"{value_kb_gb} Kb = {ans} Gb")
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
                    value_mb_kb = float(input("Enter the storage in Megabyte: "))
                    ans = round(mb_kb(value_kb_mb),2)
                    print(f"{value_mb_kb} Mb = {ans} Kb")
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
                    value_mb_gb = float(input("Enter the storage in Megabyte: "))
                    ans = round(mb_gb(value_mb_gb),2)
                    print(f"{value_mb_gb} Mb = {ans} Gb")
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
                    value_gb_kb = float(input("Enter the storage in Gigabyte: "))
                    ans = round(gb_kb(value_gb_kb),2)
                    print(f"{value_gb_kb} Gb = {ans} Kb")
                    sleep(1)
                    break
                except:
                    print("Invalid choice entered!!..\nYou'll need to start over again.")
                    sleep(1)
                    run()
               
            elif choice2==2:
                try:
                    value_gb_mb = float(input("Enter the storage in Gigabyte: "))
                    ans = round(gb_mb(value_gb_mb),2)
                    print(f"{value_gb_mb} Gb = {ans} Mb")
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

def kb_gb(value):
    ans = value/1000000
    return ans

def kb_mb(value):
    ans = value/1000
    return ans

def mb_kb(value):
    ans = value*1000
    return ans

def mb_gb(value):
    ans = value/1000
    return ans

def gb_kb(value):
    ans = value*1000000
    return ans

def gb_mb(value):
    ans = value*1000
    return ans
    
def ask_choice1():
    print("\nChoose from which unit you want to convert from: ");sleep(0.5)
    print("1. Kilobyte")
    print("2. Megabyte")
    print("3. Gigabyte\n");sleep(0.5)
    
    try:
        choice1 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice1()
    return choice1


def ask_choice2():
    print("Choose which unit you want to convert to: ");sleep(0.5)
    print("1. Kilobyte")
    print("2. Megabyte")
    print("3. Gigabyte\n");sleep(0.5)

    try:
        choice2 = int(input(">>> "))
    except:
        print("Invalid choice..")
        ask_choice2()
    return choice2

