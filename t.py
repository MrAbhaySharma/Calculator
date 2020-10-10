choice = raw_input(" What do you want to do? \n Enter:- \n \"add\" for addition \n \"sub\" for substraction \n \"multi\" for multiplication \n \"divide\" for division \n ")
def input_number():
    x1 = input("  Enter two number (in this form \"2\"):- \n  ")
    x2 = input("  ")
    return(x1,x2)
if(choice=="add"):
    n1,n2 = input_number()
    s = n1 + n2
    print("  the sum is " + str(s))
elif(choice=="sub"):
    n1,n2 = input_number()
    r = n1 - n2
    print("  the diffrence is " + str(r))
elif(choice=="multi"):
    n1,n2 = input_number()
    e = n1 * n2 
    print("  the product is " + str(e))
elif(choice=="divide"):
    n1,n2 = input_number()
    y = float(n1) / n2
    print("  the quotient is " + str(y))
else:
    print("  Wrong Choice.")