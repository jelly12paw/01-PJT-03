# import sys

# sys.stdin = open("_최빈수구하기.txt")

num_in = int(input())

for i in range(num_in) :
  score = list(map(int, input().split()))

  num = [0] * 101

  for j in score :
    num[j] += 1

  for a in range(100, -1, -1) :
    if max(num) == num[a] :
      print(f'#{i+1} {a}')
