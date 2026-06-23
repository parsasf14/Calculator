while True:
    Gogol = int(input("Type:"))
    P = int(input("Input:"))
    S = int(input("Input2:"))
    if Gogol not in range (1,5):
      print("Invalid Number!")
      continue
    if Gogol == 1:

     print(S+P)
    elif Gogol == 2:
     print(S * P)

    elif Gogol == 3:
      print (round(S / P))

    elif Gogol == 4:
      print(S - P)  