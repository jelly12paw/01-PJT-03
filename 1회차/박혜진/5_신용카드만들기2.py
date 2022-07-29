# import sys

# sys.stdin = open("_신용카드만들기2.txt")

n = int(input())
card_s = '34569'

for i in range(1, n+1) :
  card = input()

  if '-' in card :
    card = card.replace('-', '')
      
    if len(card) != 16 :
      print(f'#{i} {0}')
    
    else :
      if card[0] in card_s :
        print(f'#{i} {1}')
      
      else :
        print(f'#{i} {0}')

  else :
    if len(card) != 16 :
      print(f'#{i} {0}')
    
    else :
      if card[0] in card_s :
        print(f'#{i} {1}')
      
      else :
        print(f'#{i} {0}')
