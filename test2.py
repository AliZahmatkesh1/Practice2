a = int(input("Enter a number 1 : "))
b = int(input("Enter a number 2 : "))
c = int(input("Enter a number 3 : "))
ab = a + b
ac = a + c
bc = b + c
if ab > c and ac > b and bc > a :
    print ("\n     ***** YES *****\n")
else : print ("\n     ----- NO -----\n")
