"""
파이썬에서 가장 많이 사용되는 자료형 List
시퀀스 자료형 + Mutable자료형
"""

#List methods

S=[1,2,3]
S.append(4)
S.insert(0,2)
print (S)
print (S.index(2), S.count(2))
S.reverse()
print(S)
S.sort()
print(S)
S.remove(2) #중복이면 처음 것만 삭제
S.extend([1,2,3,4,5]) #List 추가
print(S)

# List 를 Stack 처럼 사용하기
S=[1,2,3,4]
S.append(5) # Push(5)
S.pop()

# List 를 Queue 처럼 사용하기
S=[1,2,3,4,5]
S.append(60) #Push_back
S.pop(0)    #Pop_front
print(S)

#정렬
L=[1,8,7,3,8,5,6]
L.sort()
L.sort(reverse=True)
L= 'Python is a Programming Language'.split()
L.sort()
L.sort(key=str.lower) # 대소문자 무시 정렬
L=['123','34','2345']
L.sort(key=int)

#lambda
f= lambda 입력: 입력*2
print (f(2))
L=[1,5,3,9,8,4,2]
L.sort(key=lambda a:(a%3,a))
print (L)

"""
sort()는 반환값 X
sorted()는 정렬된 리스트 반환
"""
L=[1,5,3,9,8,4,2]
R=sorted(L)
print(L,R,sep="\n")

for x in sorted(L): print(x,end=" ")

# 역순으로 참조 : reversed(L)
for x in reversed(L): print(x,end=" ")

# 리스트 내장 : List Comprehension
L = [k*k for k in range(10) if k%2==1]
print (L)
L=[(i,j,i*j) for i in range(2,100,2)
 for j in range(3,100,3)
 if (i+j)%7==0]
print(L)

print (sum(x*x for x in range(10)))

print(dir())