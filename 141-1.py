point=0		            	                   # 입력된 점수를 저장하는 변수
sum=0			                           # 합계 점수를 저장하는 변수
while (sum<20) :		                   # 합계 점수가 20점 미만이면
     point=input("다트 점수를 입력하세요.:")       # 점수를 입력
     point=int(point)		                   # 입력된 점수를 숫자형으로 변환
     print("이번 점수는", point)	           # 입력된 점수를 출력
     sum=sum+point	                           # 입력된 점수를 합계 점수에 누적
print("합계 점수는", sum)	                   # 최종 점수를 출력
