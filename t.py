choice = raw_input(" What do you want to do? \n Enter:- \n \"add\" for addition \n \"sub\" for substraction \n \"multi\" for multiplication \n \"divide\" for division \n ")
n1 = input("Enter two number (in this form \"2\"):- \n  ")
n2 = input()
if(choice=="add"):
    s = n1 + n2
    print("the sum is " + str(s))
if(choice=="sub"):
    r = n1 - n2
    print("the diffrence is " + str(r))
if(choice=="multi"):
    e = n1 + n2 
    print("the product is " + str(e))
if(choice=="divide"):
    y = n1 + n2
    print("the quotient is " + str(y))
