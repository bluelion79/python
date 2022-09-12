point=input("점수를 입력하세요.:")
point=int(point)
if (point>=90 and point<=100):      # 조건식(점수가 90 이상이고 100 이하면)
    print("성취도 A")               # 화면에 '성취도 A'를 출력
elif (point>=80 and point<=89):
    print("성취도 B")
elif (point>=70 and point<=79):
    print("성취도 C")
elif (point>=60 and point<=69):
    print("성취도 D")
else:
    print("성취도 F")
