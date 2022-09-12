price=input("빵 단가 입력:")
count=input("빵 개수 입력:")
price=int(price)
count=int(count)
total=price*count
total=total-total*0.1
print("전체 빵값:", total)
