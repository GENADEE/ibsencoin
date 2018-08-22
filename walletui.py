import client

wallet = client.wallet("wallet.dat", None, None, None, None)
while True:
  command = input()
  if command=="coins":
    i = 1
    for entry in wallet.entries:
      print(str(i)+": "+ str(entry.value))
      i += 1
  elif command[:8]=="generate":
    try:
      print("|" + " " * 20 + "|")
      n = int(command[9:])
      step = n//20 or 1
      nn = n
      while nn > 0:
        wallet.gen_keys(min(step, n))
        nn -= step
        print("|" + 20*(n-nn)//n*"=" + (20-(20*(n-nn)//n))*" " + "|")
      print("Done.")
    except ValueError:
      print("Please try again and specify the number of keys to generate.")
  elif command=="exit":
    break
  else:
    print("invalid command.")
    
