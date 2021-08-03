print("""This is a Calculator which calculates
the following operations on 2 Numbers:
  '+' for Addition
  '-' for Subtraction
  '*' for Multiplication
  '/' for Division
  '//' for Floor Division
  '**' for Exponent(Power)
  """)
def MRP_Calculator():
 try:
  def Calculator():
    Cont = int(float(input("\nDo you want to Proceed?(Yes:1/No:0): ")))
    while Cont != 1 and Cont != 0:
      if Cont != 1 and Cont != 0:
        print("It was a Yes or No Question!\n1 for Yes and 0 for No\n")
        Cont = int(float(input("Do you want to Proceed?(Yes:1/No:0): ")))
    if Cont == 1 and Cont != 0:
      num1 = float(input("Enter 1st number: "))
      num2 = float(input("Enter 2nd number: "))
      oper = input("Enter the Operator: ")
      if oper == '+':
        print("Addition of {} and {} is {}".format(num1,num2,num1+num2))
      elif oper == '-':
        print("Subtraction of {} and {} is {}".format(num1,num2,num1-num2))
      elif oper == '/':
        print("Division of {} and {} is {}".format(num1,num2,num1/num2))
      elif oper == '*':
        print("Multiplication of {} and {} is {}".format(num1,num2,num1*num2))
      elif oper == '//':
        print("Floor Division of {} and {} is {}".format(num1,num2,num1//num2))
      elif oper == '**':
        print("Division of {} and {} is {}".format(num1,num2,num1**num2))
    
    if Cont == 1 and Cont != 0:
      print("\n")
      Calculator()
    else:
      print("Thanks!\nHave a Wonderful Day or Night! :)")  
    
  Calculator() 
 except ValueError:
   print("Faulty Input! Try again")
   MRP_Calculator()
 except ZeroDivisionError:
   print("Division by Zero is not Allowed!")
   MRP_Calculator()
 except:
   print("Something else went wrong!\nRestart the Calculator :(")

MRP_Calculator()   
print("\nPlease Drop a Like and Comment ways\nin which We can Crash this Program")
