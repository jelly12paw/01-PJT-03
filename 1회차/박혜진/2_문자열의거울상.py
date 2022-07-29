# import sys

# sys.stdin = open("_문자열의거울상.txt")

for i in range(1, int(input())+1) :
  mirror = input()

  mirror = mirror.replace('b', '1') # 1 : d
  mirror = mirror.replace('d', '2') # 2 : b
  mirror = mirror.replace('p', '3') # 3 : q
  mirror = mirror.replace('q', '4') # 4 : p

  mirror = mirror.replace('1', 'd') # 1 : d
  mirror = mirror.replace('2', 'b') # 2 : b
  mirror = mirror.replace('3', 'q') # 3 : q
  mirror = mirror.replace('4', 'p') # 4 : p


  print(f'#{i} {mirror[::-1]}')