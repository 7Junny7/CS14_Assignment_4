import numpy as np

def check_value(str):
    if str.isdigit():
        return True
    else:
        print("\nInvalid data type, must be a number. Program terminated.")
        return False
def choice():
    print("Choose a conversion type:")
    print("1. Convert F to C")
    print("2. Convert C to F")
    sel = input("What is your choice? \n")
    if sel.isdigit():
        sel = int(sel)
        if not(sel == 1 or sel == 2):
            print("\nInvalid choice. Program terminated.")
            exit(0)
        return sel
    else:
        print("Invalid data type, must be a number. Program terminated.")
        exit(0)
def input_value():
    start_temp = input("Enter starting value (integer number): ")
    if check_value(start_temp):
        start_temp = float(start_temp)
    else:
        exit(1)
    end_temp = input("Enter ending value (integer number): ")
    if check_value(end_temp):
        end_temp = float(end_temp)
    else:
        exit(1)
    temp_incr = input("Enter increment value (real number): ")
    check_value(temp_incr)
    # if check_value(temp_incr):
    #     temp_incr = float(temp_incr)
    # else:
    #     exit(1)
    temp_incr = float(temp_incr)
    return start_temp,end_temp,temp_incr
def FtoC(start,end,inc):
    if start > end and inc > 0:
        print("\nInvalid range. Program terminated.")
        exit(1)
    print("{:15s}\t{:15s}".format("Fahrenheit","Celsius"))
    for F in np.arange(start,end+inc,inc):
        C = (5.0/9.0)*(F - 32.0)
        print("{:2.2f}\t\t{:2.2f}".format(F,C))

def CtoF(start,end,inc):
    if start > end and inc > 0:
        print("\nInvalid range. Program terminated.")
        exit(1)
    print("{:15s}\t{:15s}".format("Celsius","Fahrenheit"))
    for C in np.arange(start,end+inc,inc):
        F = 9.0/5.0 * C + 32.0
        print("{:2.2f}\t\t{:2.2f}".format(C,F))

if __name__ == '__main__':
    select = choice()
    start_temp, end_temp, temp_incr = input_value()

    if select == 1:
        FtoC(start_temp,end_temp,temp_incr)
    elif select == 2:
        CtoF(start_temp,end_temp,temp_incr)


