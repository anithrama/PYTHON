num=int(input("enter a number"))
month={1:"january ",2:"february ",3:"march ",4:"appril ",5:"may ",6:"june ",7:"july ",8:"august ",9:"september ",10:"october ",11:"november ",12:"december "}
if num == 1:
    print(month[1])
    print(month[1]and 31)
elif num ==2:
  print(month[2])
  print(month[2]and 29)
elif num ==3:
  print(month[3])
  print(month[3]and 30)
elif num ==4:
  print(month[4])
  print(month[4]and 31)
elif num ==5:
  print(month[5])
  print(month[5]and 30)
elif num ==6:
  print(month[6])
  print(month[6]and 31)
elif num ==7:
  print(month[7])
  print(month[7]and 30)
elif num ==8:
  print(month[8])
  print(month[8]and 31)
elif num ==9:
  print(month[9])
  print(month[9]and 30)
elif num ==10:
  print(month[10])
  print(month[10]and 31)
elif num ==11:
  print(month[11])
  print(month[11]and 30)
elif num ==12:
  print(month[12])
  print(month[12]and 31)

else:
  print("enter invalid")
  
    
    

