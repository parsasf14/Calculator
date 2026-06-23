while True:
    print("Choose A Number In : 1-6")
    print("for Tutorial Choose : 5")
    print("Exit! : 6")
    Gogol = int(input("Type:"))
    if Gogol not in range (1,7):
      print("Invalid Number!")
      continue
    if Gogol == 5:
      print("Tutorial:")
      print("1 : +")
      print("2 : *")
      print("3 : /")
      print("4 : -")
      print("5 : Tutorial")
      print("6 : Exit!")  
      continue
    elif Gogol == 6:
      print("(((Exit!)))")
      break
    num1 = int(input("Input:"))
    num2 = int(input("Input2:"))
    if Gogol == 1:

     print(num1+num2)
    elif Gogol == 2:
     print(num1 * num2)

    elif Gogol == 3:
      if num2 == 0:
        print("This is Impossible!")
        continue
      else:
        print (round(num1 / num2,2))

    elif Gogol == 4:
      print(num1 - num2)  