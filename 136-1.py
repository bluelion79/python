kind=input("승객 유형을 입력하세요. [임산부, 노약자, 일반]")
if(kind=="임산부" or kind=="노약자"):     # 조건식(임산부이거나 노약자이면)
    print("이용 가능")
else:                                     # 조건식에 맞지 않으면(임산부나 노약자가 아니면)
    print("이용 불가능")
