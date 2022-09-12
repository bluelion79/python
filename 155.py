def triangle(w,h) :		       # triangle 함수 정의
     t=(w*h)/2		               # 밑변과 높이의 값을 받아서 넓이 계산
     return t			       # 계산 결과를 반환

width=input("삼각형의 밑변:")
width=int(width)
height=input("삼각형의 높이:")
height=int(height)
area=triangle(width,height)	       # triangle() 함수를 호출, 매개 변수를 전달
print("삼각형의 넓이:", area)
