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
