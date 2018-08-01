import client

wallet = client.wallet("wallet.dat", None, None)
while True:
  command = input()
  if command=="coins":
    i = 1
    for entry in wallet.entries:
      print(str(i)+": "+ str(entry[2]))
      i += 1
  elif command[:8]=="generate":
    n = int(command[9:])
    wallet.gen_keys(n)
  else:
    print("invalid command.")
    
