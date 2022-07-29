# import sys

# sys.stdin = open("_암호문1.txt")

#1 암호코드에 삽입하는 문자 I를 기준으로 하나씩 입력해서 받아야하는 코드

sc_len = int(input())
sc = list(input().split())

num = int(input())
for i in range(1, num+1) :  
  insert_sc = list(input().split()) # 0 : I, 1 : x번째, 2 : y개, 3 ~ (3 + x-1) : 암호코드

  x = int(insert_sc[1])
  s = insert_sc[3:]


  for insert_s in s :
    sc[x] = insert_s
    x += 1

new_code = ''
for code in sc[:10] :
    new_code += code + ' '

print(f'#{i} {new_code}')

#2
# 삽입 입력코드를 모두 받기
# ValueError

for num in range(1, 11) :
  sc_len = int(input())
  sc = list(map(int, input().split()))

  insert_c_len = int(input())
  insert_c = list(input().split())

  code = []
  new_code = []
  
  for i in range(len(insert_c)) :
    if insert_c == 'I' :
      if i >= 1 :
        code.append(new_code)
    
    elif i == len(insert_c) -1 :
      new_code.append(int(insert_c[i]))
      code.append(new_code)

    else :
      new_code.append(int(insert_c[i]))

  for i in range(insert_c_len) :
    x = insert_c[i][0]
    y = insert_c[i][1]
    s = insert_c[i][2:]

    for j in range(y) :
      sc.insert(x+j, s[j])

print(f'#{num} {sc[0]} {sc[1]} {sc[2]} {sc[3]} {sc[4]} {sc[5]} {sc[6]} {sc[7]} {sc[8]} {sc[9]}')