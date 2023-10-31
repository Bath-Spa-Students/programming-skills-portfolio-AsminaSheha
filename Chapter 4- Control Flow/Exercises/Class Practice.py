#boolean expressions
sold = float(input("Enter Amount sold: "))
profit = 0
if sold > 100 :
    profit = 2000
else:
    profit = 0
print("Your Profit :   "+str(profit) )

#Nested Decision Structure
grade_in_math = int(input("Enter your marks out of 100 in Maths: "))
grade_in_English = int(input("Enter your marks out of 100 in English: "))

if grade_in_math > 50:
  if grade_in_English > 80:
         print("Congartulations, You are eligible for the scholarship")
  else :
      print("Sorry, You lack marks in English")
else : 
    print("Sorry,You lack marks in Maths")