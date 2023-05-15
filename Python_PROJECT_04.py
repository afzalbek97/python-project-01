#unit16 심사문
val = int(input())
for i in range(1,10):
	print(val,"*",i,"=",val*i)

#unit17 심사문
hav = int(input())
while hav >= 1350:
	hav-=1350
    	print(hav)

#unit18 심사문
if i>stop:
         break
     if i%10==3:
         i+=1
         continue
         
         #unit19 심사문
         height = int(input())
for i in range(height):
    for j in reversed(range(height)):
        if i < j:
            print(" ",end="")
        else:
            print("*",end="")
    for j in range(height):
        if i > j:
            print("*",end="")
    print()