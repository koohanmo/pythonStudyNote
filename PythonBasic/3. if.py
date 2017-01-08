"""
if
다른언어와 비슷한 부분이 대부분이지만
사용하기 편하게 해주는 문법들이 있음
"""

#기본 if

number =10
if number >10:
    print ("n>10")
elif number >5:
    print ("n>5")
else :
    print ("n>0")

# 1줄 짜리 if문은 한줄로 줄일 수 있다.
if number >10: print ("n>10")
elif number >5:print ("n>5")
else : print ("n>0")

# if 문을 이용해서 3항 연산자를 만들 수 있다.
a=6
x= a*2 if a>5 else a/2
print (x)

# List나 tuple을 이용해서 값을 치환 할 수 있다.(바로 위의 삼항연산자와 동치)
x= (a/2,a*2)[a>5]
print (x)

# 함수호출도 가능하다..
def add(a,b): return a+b
def sub(a,b): return a-b
sel=0
x=(add,sub)[sel](2,3)
print (x)

# Dictionary 를 이용해서 선택문을 만들 수 도 있다...
x={True:add, False:sub}[a>5](3,4)
print (x)