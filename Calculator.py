print("Hello World")
name = input("What is your name? ")
strname = str(name)
print("Hi " + strname + " great to see you here! ")
print("")
print("")
print("")
print("Welcome to Calulator")
print("Type 'S' for Sum,   'D' for Difference,     'P' for Product,       'Q' for Quotient")
operator_us = input("")
str_operator_us = str(operator_us)



print("First Number")
num_one = input("")
print("Second Number")
num_two = input("")
num_1 = int(num_one)
num_2 = int(num_two)



if str_operator_us.upper() == 'S':
    Sum = num_1 + num_2
    str_Sum = str(Sum)
    print("The Sum is " + str_Sum)
elif str_operator_us.upper() == "D":
    Difference = num_1 - num_2
    str_Difference = str(Difference)
    print("The Difference is " + str_Difference)
elif str_operator_us.upper() == "P":
    Product = num_1 * num_2
    str_Product = str(Product)
    print("The Product is " + str_Product)
elif str_operator_us.upper() == "Q":
    Quotient = num_1 / num_2
    str_Quotient = str(Quotient)
    print("The Quotient is " + str_Quotient)



else:
    print("")
    print("")
    print("Opps! Wrong Choice")

print("")
print("")
print("")
print("")
print("Let's start a quiz!")

print("")
print("")
print("")
print("")
print("Here comes the first question.")

print("")
print("")
print("")
print("")
print("When is Independence Day in India celebrated?")

print("")
print("")
print("")
print("")

print("(A) 15th March")
print("(B) 16th June")
print("(C) 15th August")
print("(D) 16th July")

print("")
print("Type A, B, C or D")
print("")
print("Answer:")

ans = str(input(""))

if ans.upper() == 'C':
    Score = 1
    print("Correct Answer")

elif ans.upper() == 'A' or 'B' or 'D':
    print("Wrong Answer!")

else:
    print("Wrong Choice!")

print("")
print("")
print("")
print("Thank You For Using My Program!")