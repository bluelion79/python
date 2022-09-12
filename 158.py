def function1() :
    global result1		            # result1을 전역 변수로 선언
    result1=num1+num2
    print("함수 안에서 결과 출력", result1)

def function2() :
    global result2		            # result2를 전역 변수로 선언
    result2=num1-num2
    print("함수 안에서 결과 출력", result2)

num1=50					    # 전역 변수 num1
num2=20					    # 전역 변수 num2

function1()				    # function1 실행, 70 정상 출력
function2()				    # function2 실행, 30 정상 출력

print("함수 밖에서 결과 출력", result1)	    # 70 정상 출력
print("함수 밖에서 결과 출력", result2)	    # 30 정상 출력
