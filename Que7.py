# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7
list_no=[]
for i in range(1,17):
    k=14
    if(i<=4):
      list_no.append(i)
    elif(i<=7):
      for j in range(0,3):
         list_no.append(0)
      list_no.append(i)
      
    elif(i==8):
       for j in range(0,3):
          
          list_no[k]=i
          i=i+1
          k-=1

    elif(i<=11):
       k=k-6
       
       list_no[k]=i
    elif(i<=12):
       k=k-10
       list_no[k]=i
    elif(i<=13):
       k=k-9
       for j in range(0,2):
          list_no[k]=i
          k=k+1
          i=i+1
    elif(i<=15):
       k=k-4
       for j in range(0,2):
          list_no[k]=i
          k=k-1
          i=i+1
          
       
       
       
       
       
    

k=0
for i in range(0,16):
   print(list_no[i],end=" ")
   k+=1
   if(k==4):
      print("")
      k=0
