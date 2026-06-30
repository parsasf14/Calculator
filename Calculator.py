def add(a,b):
  return a + b
def multiply(a,b):
  return a * b
def subtract(a,b):
  return a - b
def divide(a,b):
    if b == 0:
        return "Invalid Value!!"
    return round(a / b, 2)
def showmenu():
      print("Choose A Number In : 1-7")
      print("for Tutorial Choose : 5")
      print("Exit! : 6")
def Tutorial():
        print("Tutorial:")
        print("1 : +")
        print("2 : *")
        print("3 : /")
        print("4 : -")
        print("5 : Tutorial")
        print("6 : Exit!") 
        print("7 : Show history")

history = []

def show_menu():
    showhistory()
    hiscode = int(input("Input: "))
    if hiscode == 1:
      clearhistory()
    else: 
       hiscode == 2
       print("Lobby!!")

def showhistory(): 
  if history == []:
   print("History Is Empty!!")
  else:
    print(history)
    print("History Tutorial:")
    print("1 : Delete History")
    print("2 : Back to lobby")

def clearhistory():
  history.clear()
  print("History Deleted!!")

while True:
    showmenu()
    try:
     Gogol = int(input("Type:"))
    except:
      print("Invalid Value!!")
      continue      
    if Gogol not in range (1,8):
      print("Invalid Number!")
      continue
    if Gogol == 5:
     Tutorial()
     continue
    elif Gogol == 6:
      print("(((Exit!)))")
      break
    if Gogol == 7:
     show_menu()
     continue

    try:
     num1 = float(input("Input:"))
     num2 = float(input("Input2:"))
    except ValueError:
     print("Invalid Value!!")
     continue

    if Gogol == 1:
      result = add(num1,num2)

    elif Gogol == 2:
      result = multiply(num1,num2)

    elif Gogol == 3:
     result = divide(num1,num2)

    elif Gogol == 4:
     result = subtract(num1,num2) 

    print(f"Result:{result}")
    history.append(f"{num1} + {num2} = {result}")  