#unit12 심사문
dic_key = input().split()
dic_val = list(map(float,input().split()))
an = dict(zip(dic_key,dic_val))
print(an)

#unit13 심사문
price = int(input())
cupon = input()
if cupon == 'Cash3000':
 price -= 3000
if cupon == 'Cash5000':
 price -= 5000
print(price)

#unit14 심사문
korean, english, math, science=map(int,input().split())
x=(korean+english+math+science)/4

if (korean<0 or korean>100) or (english<0 or english>100) or (math<0 or math>100) or (science<0 or science>100):
     print('잘못된 점수')
     
else:
    if x>=80:
        print('합격')
    else:
        print('불합격')
        
        #unit15 심사문
        if 12>=age:
 balance -= 650
elif 18>=age:
 balance -= 1050
else:
 balance -= 1250
