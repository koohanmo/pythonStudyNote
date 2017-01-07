"""
주요 산술 관련 연산 정리
"""

#산술 연산자
print (5/2)
print (5//2) # 몫만  취함
print (5%2)
print (divmod(5,2)) #(몫, 나머지)
print (2**3)
print (2**3**2)

#비교연산, is와 ==의 차이

X=[1,2,3]
Y=[1,2,3]
print(X==Y)   #같은 값? True
print(X is Y) #같은 참조? False
Y=X
print(X==Y)   #같은 값? True
print(X is Y) #같은 참조? True

#List의 True/False 판별
L=[1,0,0]
print (all(L)) #모든 요소가 True이면 True
print (any(L)) #하나라도 True이면 True
