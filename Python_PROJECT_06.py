#unit25 심사문
x = {i : j for i,j in x.items() if i != 'delta' and j != 30 }

#unit26 심사문
input1, input2 = map(int,input().split())
a = {i for i in range(1,input1+1) if input1 % i == 0}
b = {i for i in range(1,input2+1) if input2 % i == 0}

#unit27 심사문
with open('words.txt','r') as f:
    a = (f.readline()).split()
    for i in a: 
        if i.find('c') != -1: 
            print(i.strip(',.'))

#unit28 심사문
a = []
with open('words.txt','r') as f: a = f.readlines()
for i in a:
    i = i.strip('\n')
    if i == ''.join(reversed(i)): 
    	print(i)