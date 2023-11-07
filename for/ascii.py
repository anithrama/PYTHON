# print(chr(65))

# for i in range(1,10):
#     k=65
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()


# k=65
# for i in range(65,70):
#     for j in range(i,0,-65):
#       print(chr(i),end="")
#     print()



#Q2

# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(i),end=" ")
#     print()


#Q3
# k=65
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()



# for i in range(64,70):
#     for j in range(i+1,64,-1):
#       print(chr(j),end=" ")
      
#     print()


#5
# n=5
# chr=65
# for i in range(1,n+1):
#     for j in range(n,i,-1):
#      print("",end="")
#     for k in range(1,i+1):
#      print(chr,end="")
#     for p in range(i,1,-1):
#      print("*",end="")
# print()



# n=6
# for i in range(6):
#     for k in range(0,n):
#         print(end="  ")
#     n-=1
#     print("*",end=" ")
#     for j in range(1,i+1):
#         print(chr(65),end=" ")
#         print("*",end=" ")
#     print()



# n=4
# for i in range(1,n+1):
#     for j in range(n,i,-1):
#         print(" ",end=" ")
#     for k in range(1,i # print("*",end=" ")+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()   


# n=6
# for i in range(6):
#     for k in range(0,n):
#         print(end="  ")
#     # n-=1
    # print("*",end=" ")
    # for j in range(1,i+1):
    #     print(j,end=" ")
    #     # print("*",end=" ")
    # print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,i,i+1):
        
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#             for k in range(1,n+1):
#   print()




# b=3
# a=(b*2)+1
# for i in range(a):
#     for k in range(0,1):
#       print("*",end=" ")
#     if i<b:
#         for m in range(1,i+1):
#           print(m,end=" ")
#         for j in range(i-1,0,-1):
#             print(j,end=" ")
#     if i>=b:
#         for n in range(1,b):
#              print(n,end=" ")
#         for o in range(b,0,-1):
#             print(o,end=" ")
#         b=b-1
#     if i>0 and i<a-1:
#             for l in range(0,1):
#                 print("*",end=" ")
#     print()
#     print()



def pattern1():
 k=1
 for i in range(5):
    for j in range(1,k+1):
        print('*',end="")
    k=k+2
    print()

def pattern2():
 for i in range(5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



pattern2()






