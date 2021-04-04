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
