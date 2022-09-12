point=0			                          # 입력된 점수를 저장
total=0			                          # 최종 점수를 저장
for i in range(1,21,1) :		          # 1부터 20까지 20회 반복
     text=str(i)+"회 다트 점수를 입력하세요.:"	  # 입력 안내
     point=input(text)		                  # 점수를 입력
     point=int(point)		                  # 입력된 점수를 숫자형으로 변환
     print(i, "회 점수는", point)	          # 입력된 점수를 출력
     total=total+point	                          # 입력된 점수를 최종 점수에 누적
print("최종 점수는", total)	                  # 최종 점수를 출력
