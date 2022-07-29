# import sys

# sys.stdin = open("_신용카드만들기1.txt")

n = int(input())

for i in range(1, n+1) :
  card = list(map(int, input().split()))

  for j in range(16) :
    if j % 2 == 0 :
      card[j] = card[j] * 2

      for six in range(10) :
        if (sum(card) + six) % 10 == 0 :
          s = six
  
  print(f'#{i} {s}')