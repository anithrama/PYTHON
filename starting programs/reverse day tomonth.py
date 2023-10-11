num=int(input("enter no:of days"))
day={31:["jan","march","may","july","sep","november"],
      29:["feb"],
      28:["feb"],
      30:["april","june","august","october","dec"]}
if num==31:
    print(day[31])
elif num==29:
    print(day[29])
elif num==28:
    print(day[28])
elif num==30:
    print(day[30])
else:
    print("enter invalid")
