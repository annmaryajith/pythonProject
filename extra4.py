f = open("deoo.txt", "r")
if f.closed == True:
  print("File is closed")
else:
  print("File is open")
f.close()
if f.closed == True:
  print("File is closed")
else:
  print("File is open")