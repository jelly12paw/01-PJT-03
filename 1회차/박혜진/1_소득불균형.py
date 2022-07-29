# import sys

# sys.stdin = open("_소득불균형.txt")

TC = int(input())

for i in range(1, TC+1) :
  TC_len = int(input())
  num = list(map(int, input().split()))

  cnt = 0
  for j in num :
    mean = sum(num) // TC_len
    if j <= mean :
      cnt += 1
  
  print(f'#{i} {cnt}')
