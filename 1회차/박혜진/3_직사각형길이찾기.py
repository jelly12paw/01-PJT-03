# import sys

# sys.stdin = open("_직사각형길이찾기.txt")

a = int(input())

for i in range(1, a+1) :
    b, c, d = map(int, input().split())
    
    if b == c :
        print(f'#{i} {d}')

    elif b == d :
        print(f'#{i} {c}')

    elif c == d :
        print(f'#{i} {b}')

    else :
        if b == c == d :
            print(f'#{i} {b}')