kind=input("종류를 입력하세요. [사람, 개, 고양이, 새]")
if(not kind=="사람"):         # 조건식(사람이 아니면)
    print("운송 용기 사용")
else:                         # 조건식에 맞지 않으면(사람이면)
    print("운송 용기 미사용")
