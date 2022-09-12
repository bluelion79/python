def stick_game(a):
    if (a==1):
        b="도"
    elif (a==2):
        b="개"
    elif (a==3):
        b="걸"
    elif (a==4):
        b="윷"
    else:
        b="모"
    print("결과:", b)
    print("이동 거리:", a)

import random
a=random.randint(0, 4)
print("뒤집힌 막대의 개수:", a)
stick_game(a)

# 15~16번 줄은 0~4 사이에서 임의의 숫자를 구하는 코드
