age=input("나이를 입력하세요.:")
age=int(age)
fee=14000
if (age<=10):
    fee=fee*0.8
elif (age>=60):
    fee=fee*0.7
else:
    fee=fee*1
print("이용 요금:", fee)
