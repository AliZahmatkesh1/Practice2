import math

                          #### Python 3 ####


aa = "true"
while aa == "true" :
    print ("Baraye bastan (Exit) type konid.")
    bb = input("Enter (calculator = c / triangle = t / average = a ). \n_:").strip().lower()

#tamrin 1

    if bb == "c" or bb == "calculator" or bb == "cal" :
        while aa == "true":
            a = int(input("Enter a number 1 : ").strip())
            b = int(input("Enter a number 2 : ").strip())
            print("\nEnter (+,-,*,/,radical = rad,sin,cos,tan,cot,factorial = fac).")
            print ("Baraye bastan (Exit) , baraye raftan be meno (Meno) type konid.") 
            op = input("Baraye khoroji hame az (all) estefade konid. \n_: ").strip().lower()
            a1 = str(a)
            b1 = str(b)
            if op == "+" :
                print ("\nAddition "+a1+" + "+b1+" =",(a + b))
                print ("\n")
            elif op == "-" :
                print ("\nSubtraction "+a1+" - "+b1+" =", (a - b))
                print ("\n")
            elif op == "*" :
                print ("\nMultiplication "+a1+" * "+b1+" =", (a * b))
                print ("\n")
            elif op == "/" :
                if b :
                    print ("\nDivision "+a1+" / "+b1+" =", (a / b))
                    print ("\n")
                else :
                    print ("\n     ----- NO -----")
                    print ("\n")
            elif op == "rad" or op == "radical" :
                print ("\nRadical "+a1+" =",math.sqrt(a))
                print ("Radical "+b1+" =",math.sqrt(b))
                print ("\n")
            elif op == "sin" :
                print ("\nSin "+a1+" =",math.sin(a))
                print ("Sin "+b1+" =",math.sin(b))
                print ("\n")
            elif op == "cos" :
                print ("\nCos "+a1+" =",math.cos(a))
                print ("Cos "+b1+" =",math.cos(b))
                print ("\n")
            elif op == "tan" :
                print ("\nTan "+a1+" =",math.tan(a))
                print ("Tan "+b1+" =",math.tan(b))
                print ("\n")
            elif op == "cot" :
                if a :
                    print ("\nCot "+a1+" =",math.cos(a) / math.sin(a))
                else :
                    print ("\n     ----- NO -----")
                    print ("\n")
                if b :
                    print ("Cot "+b1+" =",math.cos(b) / math.sin(b))
                    print ("\n")
                else :
                    print ("     ----- NO -----\n") 
            elif op == "fac" or op == "factorial" :
                print ("\nFactorial "+a1+" =",math.factorial(a))
                print ("Factorial "+b1+" =",math.factorial(b))
                print ("\n")

    # all
            elif op == "all" :
                print ("\nAddition "+a1+" + "+b1+" =", (a + b))
                print ("\nSubtraction "+a1+" - "+b1+" =", (a - b))
                print ("\nMultiplication "+a1+" * "+b1+" =", (a * b))
                if b :
                    print ("\nDivision "+a1+" / "+b1+" =", (a / b))
                print ("\nRadical "+a1+" =",math.sqrt(a))
                print ("Radical "+b1+" =",math.sqrt(b))
                print ("\nSin "+a1+" =",math.sin(a))
                print ("Sin "+b1+" =",math.sin(b))
                print ("\nCos "+a1+" =",math.cos(a))
                print ("Cos "+b1+" =",math.cos(b))
                print ("\nTan "+a1+" =",math.tan(a))
                print ("Tan "+b1+" =",math.tan(b))
                if a :
                    print ("\nCot "+a1+" =",math.cos(a) / math.sin(a))
                if b :
                    print ("Cot "+b1+" =",math.cos(b) / math.sin(b))
                print ("\nfactorial "+a1+" =",math.factorial(a))
                print ("factorial "+b1+" =",math.factorial(b))
                print ("\n")
    # break
            elif op == "meno" :
                print ("\n\n")
                break
    # exit
            elif op == "exit" :
                exit()
    # error
            else :
                print ("\n\nError ....... vorodi na moshakhas.\n\n")

#tamrin 2
                
    elif bb == "t" or bb == "triangle" : 
        print ("\n Example : 3 , 5 , 7 => true\n") 
        a = int(input("Enter a number 1 : "))
        b = int(input("Enter a number 2 : "))
        c = int(input("Enter a number 3 : "))
        ab = a + b
        ac = a + c
        bc = b + c
        if ab > c and ac > b and bc > a :
            print ("\n     ***** YES *****\n")
        else : print ("\n     ----- NO -----\n")

#tamrin 3
        
    elif bb == "a" or bb == "average" :
        fname = input("\nPlease enter your name?\n--").strip().upper()
        lname = input("\nPlease enter your lastname?\n--").strip().upper()
        Lesson1 = float(input("\nPlease enter your grade 1 ?\n--").strip())
        Lesson2 = float(input("\nPlease enter your grade 2 ?\n--").strip())
        Lesson3 = float(input("\nPlease enter your grade 3 ?\n--").strip())

        average = (Lesson1 + Lesson2 + Lesson3)/3
        if average >= 17 :
            print ("\n\n     *****OPS*****")
            print ("********GREATE********")
            print ("Dear "+fname+" "+lname+" ,your grade point average in three subjects was ("+str(round(average,2))+")")
            print("and you got an (Greate) grade.")
            print ("\n\n")
        elif average < 17 and average >= 12 :
            print ("\n\n     ********NORMAL********")
            print ("Dear "+fname+" "+lname+",your grade point average in three subjects was ("+str(round(average,2))+")")
            print("and you got an (NORMAL) grade.")
            print ("\n\n")
        elif average < 12 :
            print ("\n\n     ********FAIL********")
            print ("Dear "+fname+" "+lname+",your grade point average in three subjects was ("+str(round(average,2))+")")
            print("and you got an (FAIL) grade.")
            print ("\n\n")
    # exit
    elif bb == "exit" :
        exit()
    # error
    else:
        print ("\n\nError ....... Enter ( c , t , a )\n\n")

############### Ali Zahmatkesh ###############
