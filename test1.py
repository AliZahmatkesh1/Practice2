import math
a = int(input("Enter a number 1 : ").strip().lower())
b = int(input("Enter a number 2 : ").strip().lower()) 
op = input("\nEnter (+,-,*,/,radical = rad,sin,cos,tan,cot,factorial = fac , all).\n-- ").strip().lower()
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
input()
