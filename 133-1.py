card=input("카드 잔액을 입력하세요.")	# 프로그램이 입력을 기다림
card=int(card)				# 입력된 잔액을 숫자형으로 변환
if (card>=1000) :                       # 조건식(카드 잔액이 1000보다 크거나 같으면)
    print("버스 탑승 가능")
else :                                  # 조건식에 맞지 않으면(카드 잔액이 1000보다 작으면)
    print("버스 탑승 불가")
