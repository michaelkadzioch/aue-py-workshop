if __name__ == "__main__":
  summe = 0

  eingabe = input('Geben Sie eine Zahl ein: ')

  try:
    zahl = int(eingabe)
    summe = 10 + zahl
  except:
    print('Es wurde keine gültige Zahl eingegeben.')

  print(summe)