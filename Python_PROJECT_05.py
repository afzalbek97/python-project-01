#unit20 심사문
mn, mx = map(int,input().split())
for i in range(mn,mx+1):
    print("Fizz" * (i % 5 == 0) + "Buzz" * (i % 7 == 0) or i)

#unit21 심사문
for i in range(n):   
    t.forward(line)    
    t.right((360/n)*2)   
    t.forward(line)    
    t.left(360/n)

#unit22 심사문
start, last = map(int,input().split())
answer=[2 ** i for i in range(start, last + 1)]
del answer[1]
del answer[-2]
print(answer)

#unit23 심사문
matrix = []; answer = [] #;를 이용해 2줄의 명령을 1줄로 줄었다.(꼼수..)
col, row = map(int,input().split()) #입력
for i in range(row): matrix.append(list(input())) #col,row 만큼 입력 받는 코드
for i in range(col):
    for j in range(row):
        tmp = 0
        if matrix[i][j] == '.': #해당 인덱스가 '.'(지뢰가 아닐) 경우
            if (i-1) >= 0: tmp += 1 if matrix[i-1][j]=='*' else 0 #if문을 한줄로 씀으로서 길이를 줄였다.
            if (j-1) >= 0: tmp += 1 if matrix[i][j-1]=='*' else 0 
            if (i+1) < col : tmp += 1 if matrix[i+1][j]=='*' else 0
            if (j+1) < row : tmp += 1 if matrix[i][j+1]=='*' else 0
            if (i-1) >= 0 and (j-1) >= 0: tmp += 1 if matrix[i-1][j-1]=='*' else 0
            if (i+1) < col and (j+1) < row: tmp += 1 if matrix[i+1][j+1]=='*' else 0
            if (i+1) < col and (j-1) >= 0 : tmp += 1 if matrix[i+1][j-1]=='*' else 0
            if (i-1) >= 0 and (j+1) < row : tmp += 1 if matrix[i-1][j+1]=='*' else 0
            answer.append(tmp); 
        else: answer.append('*') #지뢰일 경우 * 그대로 출력
        #;를 이용해 2줄의 명령을 1줄로 줄었다.(꼼수..)
count = row #row의 수 만큼 나눠서 출력하기 위해 변수 하나 생성
for i in range(len(answer)):
    if i >= row : row+=count; print() #;를 이용해 2줄의 명령을 1줄로 줄었다.(꼼수..)
    print(answer[i],end="")

#unit24 심사문
string = input().split(' ')
count = 0
for i in string:
    if i.strip(',.') == 'the':
        count += 1
print(count)

#unit24 심사문
price = list(map(int,input().split(';')))
price.sort(reverse=True)
for i in price:
    print('{:>9,d}'.format(i))
