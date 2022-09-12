def function1() :
    result1=num1+num2
    print("함수 안에서 결과 출력", result1)	

def function2() :
    result2=num1-num2
    print("함수 안에서 결과 출력", result2)	

num1=50					    # 전역 변수 num1
num2=20					    # 전역 변수 num2

function1()				    # function1 실행, 70 정상 출력
function2()				    # function2 실행, 30 정상 출력

print("함수 밖에서 결과 출력", result1)	    # 실행 오류
print("함수 밖에서 결과 출력", result2)	    # 실행 오류
