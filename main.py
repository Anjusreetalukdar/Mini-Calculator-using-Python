while True:
    w = input("what you want +,-,*,/,%,s(sqrt),sq(square),off:")
    if w == "off":
        print('off')
        break
    v1 = int(input("Enter first no:"))
    v2 = int(input("Enter 2nd no"))

    if w == "off":
        break    
    elif w == "+":
        print('Add',v1+v2)
    elif w == "-":
        print("subtract",v1-v2)
    elif w == "*":
        print("multiply",v1*v2)
    elif w == "/":
        print("div",v1/v2)
    elif w == "%":
        print("reminder",v1%v2)
    elif w == "s":
        print("sqrt",v1*0.5,v2*0.5)
    elif w == "sq":
        print("square",v1*v1,v2*v2)
    else:
        print("please enter valid operation")