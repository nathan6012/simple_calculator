from   cal_logic import add,sub,multi,div
while True:
  try:
    print("_____________________________")
    operators = input("""Select Operator
    (  + , x , ÷, -  )
   press  A to exit : """)
    
    if operators == "A" or operators =="a":
      print("Closing Calculator\n ")
      break 
      exit()
  except NameError:
    print("Wrong operator")
 
  
  #Num 1 # num1 ###############
  numy = input("1st Numebr: ")
  num1 = int(numy)
  
 # num2 ###############################
  numx = input("2nd Number:")
  num2 = int(numx)
  print()
  
  
# Flow Control ###################€€
  if operators =="+":
    print("answer",add(num1,num2))
    print()
  elif operators =="x" or operators =="X":
    print("answer",multi(num1,num2))
    print()
  elif operators =="÷" or operators =="/":
    print("answer",div(num1,num2))
    print()
  elif operators =="-":
    print("answer",sub(num1,num2))
    print()

  