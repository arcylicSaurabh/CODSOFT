a= int(input("first number is :"))
b= int(input("second number is :"))
operator = input("operator is :")
match operator :
     case "+" : 
          print("sum is :",a+b)
     case "-" : 
          print("subtraction  is :",a-b)
     case "*" : 
          print("multiplication is :",a*b)
     case "**" : 
          print("exponentiation is :",a**b)
     case "//" : 
          print("floor division is :",a//b)
     case "%" : 
          print("modulus  is :",a%b)