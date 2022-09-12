sum=0				     # 합계 변수
f=open("input.txt","r")	             # input.txt 파일 열기
lines=f.readlines()	             # 파일 전체 내용 가져오기
for i in range(0,len(lines)):	     # 줄 수만큼 반복
	num=int(lines[i])	     # 한 줄을 숫자로 변환
	print(num)		     # 숫자를 출력
	sum=sum+num	             # 숫자를 합계 변수에 더하기
print("합계:", sum)		     # 전체 숫자가 더해진 합계 출력
f.close()			     # input.txt 파일 닫기

f=open("output.txt","w")	     # output.txt 파일 열기
f.write("합계:"+str(sum))	     # 파일에 결과 저장
f.close()			     # output.txt 파일 닫기
