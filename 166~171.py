# 입력 자료 준비하기
in2006=[];in2007=[];in2008=[];in2009=[];in2010=[]	# 2006~2015 연도별 외국인여행자 수 저장 배열
in2011=[];in2012=[];in2013=[];in2014=[];in2015=[]
out2006=[];out2007=[];out2008=[];out2009=[];out2010=[]	# 2006~2015 연도별 해외여행자 수 저장 배열
out2011=[];out2012=[];out2013=[];out2014=[];out2015=[]

def ready() :						# 함수 정의
     f=open("traveler.csv","r")			        # 연도별 여행자 자료가 저장된 CSV 파일 열기
     csvReader=csv.reader(f)				# CSV 파일로부터 내용 읽어오기
     for row in csvReader:				# 한 줄씩 모든 자료에 대해 반복
          for i in range(1,len(row)):			# 1월~12월 자료에 대해 반복
               eval(row[0]).append(int(row[i]))		# 배열에 월별 자료 추가
     f.close()						# 파일 닫기


# 월별 합계, 월별 평균 계산하기
insum=[0,0,0,0,0,0,0,0,0,0,0,0]			# 외국인여행자 통계 배열 (월별 합계)
inavg=[0,0,0,0,0,0,0,0,0,0,0,0]			# 외국인여행자 통계 배열 (월별 평균)
outsum=[0,0,0,0,0,0,0,0,0,0,0,0]		# 해외여행자 통계 배열 (월별 합계)
outavg=[0,0,0,0,0,0,0,0,0,0,0,0]		# 해외여행자 통계 배열 (월별 평균)

def calc() :
     for i in range(0,12) :
          insum[i]=in2006[i]+in2007[i]+in2008[i]+in2007[i]+in2009[i]+in2010[i]+in2011[i]+in2012[i]+in2013[i]+in2014[i]+in2015[i]	           # 외국인여행자 통계 계산(월별 합계)
          outsum[i]=out2006[i]+out2007[i]+out2008[i]+out2007[i]+out2009[i]+out2010[i]+out2011[i]+out2012[i]+out2013[i]+out2014[i]+out2015[i]	   # 해외여행자 통계 계산(월별 합계)

     for i in range(0,12) :
          inavg[i]=insum[i]/10			 # 외국인여행자 통계 계산(월별 평균)
          outavg[i]=outsum[i]/10		 # 해외여행자 통계 계산(월별 평균)


# 사용자 입력
def user_select() :
     global line1, line2		                      # 꺾은선 그래프1, 꺾은선 그래프2를 전역 변수로 선언
     global info1, info2	                              # 꺾은선 그래프1의 범례, 꺾은선 그래프2의 범례를 전역 변수로 선언
     print("\n한국관광공사의 자료를 이용해서 그래프를 보여줍니다.\n")
     print("1. 10년간 외국인여행자 수의 평균과 해외여행자 수의 평균을 월별로 비교")
     print("2. 10년간 외국인여행자 수의 평균과 선택한 연도의 외국인여행자 수를 월별로 비교")
     print("3. 10년간 해외여행자 수의 평균과 선택한 연도의 해외여행자 수를 월별로 비교")
     print("4. 선택한 연도의 외국인여행자 수와 해외여행자 수를 월별로 비교")

     kind=input("\n원하는 그래프의 번호를 입력하세요.: ")     # 사용자의 선택 대기
     kind=int(kind)			             	      # 입력된 값을 정수로 변경
     
     if (kind==1) :
          print("\n10년간 외국인여행자 수의 평균과 해외여행자 수의 평균을 월별로 비교하는 그래프입니다.\n")
          line1=insum			                      # 꺾은선 그래프1에 외국인여행자 수의 월별 합계
          line2=outsum		                              # 꺾은선 그래프2에 해외여행자 수의 월별 합계
          info1="Total In"
          info2="Total Out"
     elif (kind==2) :
          year = input("\n연도를 입력하세요.: ")
          print("\n10년간 외국인여행자 수의 평균과 선택한 연도의 외국인여행자 수를 월별로 비교하는 그래프입니다.\n")
          line1=inavg		                              # 꺾은선 그래프1에 외국인여행자 수의 평균
          line2=eval("in"+year)                               # 꺾은선 그래프2에 선택한 연도의 외국인여행자 수
          info1="Average In"
          info2=year+" In"
     elif (kind==3) :
          year=input("\n연도를 입력하세요.: ")
          print("\n10년간 해외여행자 수의 평균과 선택한 연도의 해외여행자 수를 월별로 비교하는 그래프입니다.\n")
          line1=outavg		                              # 꺾은선 그래프1에 해외여행자 수의 평균
          line2=eval("out"+year)	                      # 꺾은선 그래프2에 선택한 연도의 해외여행자 수
          info1="Average Out"
          info2=year+" Out"
     elif (kind==4) :
          year=input("\n연도를 입력하세요.: ")
          print("\n선택한 연도의 외국인여행자 수와 해외여행자 수를 월별로 비교하는 그래프입니다.\n")
          line1=eval("in"+year)	                              # 꺾은선 그래프1에 선택한 연도의 외국인여행자 수
          line2=eval("out"+year)	                      # 꺾은선 그래프2에 선택한 연도의 해외여행자 수
          info1=year+"In"
          info2=year+"Out"


# 그래프 출력
def graph() :
     maxline=max(line1,line2)	                                # 최대 상태값을 갖는 꺾은선 그래프 구함
     minline=min(line1,line2)	                                # 최소 상태값을 갖는 꺾은선 그래프 구함
     maxv=max(maxline)	        	                        # 최대 상태값 구함
     minv=min(minline)	                  	                # 최소 상태값 구함
     maxv=maxv+(maxv*0.1)	                                # 그래프의 최대 눈금 계산
     minv=minv-(minv*0.2)	                                # 그래프의 최소 눈금 계산
     
     month=range(1,13)	                                        # 그래프 월 설정
     mplot.plot(month,line1,month,line2,marker="o")             # 그래프 작성
     
     mplot.axis(xmin=1,xmax=12,ymin=minv,ymax=maxv)             # X축과 Y축의 눈금 설정
     
     mplot.title("Compare Travelers")	                        # 그래프의 제목 설정
     mplot.xlabel("Month")	                                # X축의 제목 설정
     mplot.ylabel("Person")	                                # Y축의 제목 설정
     
     mplot.legend([info1,info2],loc='lower right')	        # 범례 설정
     
     mplot.show()			                        # 그래프 인쇄


# 프로그램 실행
import csv				# csv 파일 모듈 사용
import matplotlib.pyplot as mplot	# 파이선 그래프 모듈 사용
ready()				        # 자료 준비 기능 함수 호출
calc()				        # 계산 기능 함수 호출
user_select()		                # 사용자 선택 처리 기능 함수 호출
graph()				        # 그래프 출력 기능 함수 호출
