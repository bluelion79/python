# -*- coding: utf-8 -*-
"""20908 김혜은 정보 수행 (학교 문제 해결)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LoR8KWJMEOFoDd2mzzV3igkKS9fZfjFN

# **1. 문제의 분석과 추상화(단순화) 2점**

가. 문제의 분석

**<현재 상태>**

  학교의 운동장에 학교 관계자분들의 자가용이 가득 차서 운동장을 본래 목적(체육공간)으로 활용하지 못하고 있음. 결정이 필요한 상황에서 선생님이 갈팡질팡하시는 상황.

  **<목표 상태>**

  선생님들의 차를 주차하면서도 아이들이 운동장을 확보할 수 있도록 하는 것. (선생님들이 주차를 한 후에 교무실에 들어가시는 일련의 과정을 코딩함.) ...선생님들이 학교에 도착한 후 교무실에 들어가실 때까지 발생할 수 있는 문제상황(결정이 필요한 사항)에 대해 코딩.

나. 추상화(단순화)

**<작은 문제로 분해>**
- 환영인사

- 오늘이 무슨 요일인지 묻기

- 본인의 차랑변호 맨 앞자리 수를 묻기

- 요일과 숫자에 따라 대답 달리하기.

- 주차를 학교에 못 하는 경우, 다른 주차장을 안내함.

- 주차를 끝냈다는 가정 하에, 계단을 이용할지 엘리베이터를 탈지 조사

- 엘리베이터의 경우 사람 수(랜덤)으로 한 후 7명 이하면 탐.

- 엘리베이터에 탔다는 가정 하에, 몇 층을 가실지 조사.

- n층에 도착 후, 학생을 마주친 상황.. 인사를 할 것인지 말 것인지 결정.

- 무사히 교무실에 도착.


**<모델링>**
- 환영인사 (성명을 넣어서 )

- 오늘이 무슨 요일인지 묻기 (월,화,수,목,금,토,일)

- 본인의 차랑변호 맨 앞자리 수를 묻기 (0 ~9)

- 요일과 숫자에 따라 대답 달리하기. (월수금 / 화목 / 토일)

- 주차를 학교에 못 하는 경우, 다른 주차장을 안내함. (주변 주차장 안내)

- 주차를 끝냈다는 가정 하에, 계단을 이용할지 엘리베이터를 탈지 조사

- 엘리베이터의 경우 사람 수(랜덤)으로 한 후 7명 이하면 탐. 

- 엘리베이터에 탔다는 가정 하에, 몇 층을 가실지 조사. (2, 3, 4)

- n층에 도착 후, 학생을 마주친 상황.. 인사를 하자 ( 안녕 )

- 무사히 교무실에 도착.

# **2. 문제 해결 전략 설계 3점**

1) **시작**

2) 환영인사 (함수)

3) 요일 물어서 조건문 나누기 (조건문)**

4) 차량 맨 앞자리가 홀수인지 짝수인지 파악 ()(for문)**

5) 홀, 짝에 따라 말 달리하기.(조건구문)**

6) 주차완료하면 엘베타러감

7) 사람 수에 따라 7명 이하가 되면 탐. (for문)**

8)몇층에 갈건지를 조사 (함수)**

9) 학생을 마주침. 인사하기 (함수)

10) 종료

# **3. 프로그래밍 15점**

모든 코드는 실행이 되는 것이 원칙입니다. 실행이 되지 않는 코드를 단순 복사해서 사용하면 0점 처리합니다.

- 함수: 1~2개 사용 1.5점, 3개 이상 사용 3점, 미사용 0점 
- 변수: 사용 3점, 미사용 0점 
- if(조건문): 1~2개 사용 1.5점, 3개 이상 사용 3점, 미사용 0점 
- for, while(반복문): 1~2개 사용 1.5점, 3개 이상 사용 3점, 미사용 0점 
- 창의성 및 완성도: *교과서 또는 인터넷에 있는 것 그대로 사용 0.5점*, *주석 없는 단순 수정 1점*, *창의성 및 복잡성 및 완벽한 주석 처리 1.1점~3점*
"""

"""
20908 김혜은
영신여고 운동장 차량 점령 문제 해결 ( 추가로 선생님의 교무실 무사 도착 시뮬레이션까지..)

함수, 변수, for(반복구문), if(조건구문), 절차구문
모두 활용해서 프로그램을 완성하기
"""

###영신여고 운동장 자동차 점령 문제상황을 해결하기 위한 코딩. (추가로 선생님의 안전 교무실 도착 시뮬레이션까지..여러 사소한 문제들 포함)

## 골목을 지나 영신여고 정문으로 들어가는 중. (본인은 선생님이고 차량을 타고 옴.)

def greet(name):          #1 선생님의 성명을 입력하시는겁니다..(사실 원래는 차량번호 입력하면 대응되는 이름이 뜨게 하려고 했는데 계속 오류가..)

    print("안녕하세요, " + name + "선생님. 영신여고에 어서오세요")  #영신여고에 들어오면서 인사받기
greet(input("선생님성명: "))

import time
time.sleep(3)                          # 슬립이 없으면 너무 빨리 진행이 되어서 이해를 돕기 위해 넣음

## 오늘에는 주차를 어디에 해야하는지 모르는 문제가 생긴 상황. 코딩기계를 이용해보자.

while True:                            # 요일 주차제도 시행 ( 홀수 번호, 짝수번호 )

    a=(int(input("오늘은 무슨 요일인가요(월,화,수,목,금,토,일 각각 1부터 7의 수로 입력)?= " )))  #요일변수
    b=(int(input("차량번호의 맨앞자리 수를 입력하세요.= " )))                                    #차량번호변수

    if ( a<3 ) :                       #월요일 또는 화요일인 것임. 월,화는 홀수차가 주차하는 날.

         if (b%2 == 1): 
              print('영신여고 운동장 가장자리에 질서를 지켜 주차해주십시오.')
                                      #학생들이 체육을 할 수 있는 공간을 마련하기 위해 질서를 지켜서 주차하기.
         else :
              print('죄송합니다만, 오늘은 짝수차량이 주차하실 수 없습니다. 가까운 공용주차장을 이용해주시길 바랍니다. 02-0101-3939')
                                       #주변 공욜주차장의 번호를 제시.

    elif ( a>=3 and a<6) :             #수요일 또는 목요일 또는 금요일인 것임. 수,목,금은 짝수차가 주차하는 날.

           if (b%2 ==1):
               print('죄송합니다만, 오늘은 홀수차량이 주차하실 수 없습니다. 가까운 공용주차장을 이용해주시길 바랍니다. 02-0101-3939')
           else :
               print('영신여고 운동장 가장자리에 질서를 지켜 주차해주십시오.')

    elif ( a>=6 ) :                    #토요일 또는 일요일인 것임. 토,일은 모든 차량 주차 가능한 날.

        print('오늘은 학생이 없어 모든 차량이 주차 가능합니다. 교회나 학교에 방문한 분들 모두 환영합니다.')
                                       #토,일엔 5층 교회에 방문하신 분들이 많으실거라 생각.

    next_calculation = input("주차를 완료하셨습니까? (yes/no): ") 
    if next_calculation == "yes":
         break                          #주차 완료했다면 while문 종료
    
    else:
          print("빨리 하시길...")       #ㅎ

## 엘리베이터에 타러 온 상황. 7명 미만이면 타자. (인원초과 문제상황이 생길 것을 대비하자.)

print('엘리베이터를 타러 가야겠다')

import time
time.sleep(3)                           #이해 돕기용 (속도 조절)

import random

for i in range(1):
  c= random.randint(0,9)                                              #다른 함숫값 입력 없이 랜덤으로 학생 수가 정해짐.

  if ( c<7 ):   
    print('엘리베이터 대기 인원이 7명 미만이니까 이번에 타자.')       #랜덤으로 정해진 수에 의해 바로 답변이 뜨게 됨.

  else:
    print('아..이런, 엘리베이터 대기수가 너무 많군. 좀만 기다리자.')

import time
time.sleep(3)                          #속도 조절

# 엘리베이터에 탄 상황. 무사히 교무실까지 가자.

print('후..드디어 탔군.')

import time
time.sleep(1)                          #속도 조절

def elevator(floor):                                       # 엘리베이터에서 학생에게 층수를 알려주기

    print( "선생님, 몇층에 가시나요?" )                    # 학생이 버튼을 대신 눌러드림.

    import time
    time.sleep(2)                                          # 대화 상황이 자연스럽게 말 사이에 텀 두기.

    print( "난" + floor + "층에 간단다.")                  # 교무실 층수 말해주기.

elevator(input("교무실층수: "))

import time
time.sleep(3)

## 교무실에 들어가려는 찰나, 학생을 마주친 상황.

print('교무실 앞에 학생이 있네..')
def greet(student):                                        # 학생을 복도에서 마주쳤다. 인사해야지

    print("안녕, " + student + ". 좋은 하루 보내렴")       # 먼저 인사해서 인기쟁이 선생님 등극
greet(input("학생이름: "))

import time
time.sleep(1)                                              #학생이 대답할 때까지 시간 차 두기.

print("네, 선생님도요!")                                   #학생이 선생님의 인사에 대답함.

import time
time.sleep(3)                                              #선생님이 교무실에 들어가서 앉는 동안의 시간.

# 교무실에 도착해 본인의 자리에 착석함. 플래너를 꺼내고 하루 다짐을 쓰자.

print('플래너에 하루덕담을 적어볼까?')                     #덕담에 쓰실 것 같은 내용을 추측해서 만들어봄.

planner = input("내 이름은 (제샛별/김준오/정원섭): ")      #선생님은 3명인걸로 가정..
if (planner == "정원섭"):
  mytuple = ('공부는', '엄마주도학습이 아닌', '학원주도학습도 아닌', '자기주도학습')
  for x in mytuple:   
  	print(x)
 
elif (planner == "김준오"):
  mytuple = ('오늘도', '뮤지컬 같은', '하루가', '되길')
  for y in mytuple:   
	  print(y)
 
elif (planner == "제샛별"):
  mytuple = ('하루의', '시작은', '상쾌한', '스트레칭으로')
  for z in mytuple:   
  	print(z)
   
import time
time.sleep(6)