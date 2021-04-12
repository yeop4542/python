# Quiz 1

station = "사당"
print(station, "행 열차가 들어오고 있습니다.") 
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.") 
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.") 

# Quiz 2

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월",str(date),"일로 선정되었습니다")

# Quiz 3

adress = "http://naver.com"
x = adress.replace("http://", "")
y = x.index(".")
z = x[:y]
password = z[:3] + str(y) + str(z.count("e")) + "!"
print("{}의 비밀번호는 {}입니다." .format(adress, password))

# Quiz 4

print(' -- 당첨자 발표 -- ')
from random import *
people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(people)
x = sample(people, 4)
print("치킨 당첨자 : {}".format(x[0]))
print("커피 당첨자 : {}".format(x[1:]))
print(" -- 축하합니다 -- ")

# Quiz 5

from random import *
x = 0
for y in range(1, 51):
    t = randrange(5, 51)
    if 5 <= t <= 15:
        a = "[O]"
        x += 1
    else:
        a = "[ ]"
    print("{} {}번째 손님 (소요시간 : {}분)".format(a, y, t))
print("총 탑승 승객 : {} 분".format(x))



       
 
