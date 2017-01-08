"""
파이썬의 주석은 #(라인) 과 (""" """)(블록) 을 사용할 수 있다.
"""

# input

name = input('name?')
print (name)

#정수 값 입력받기
n = int(input('int : '))
print (n, type(n))

#줄바꾸기 하지 않고 print 마지막에 취하는 자동처리 문자 바꾸기
print (1,2); print (3,4)        #두줄로 출력이 된다.
print(1,2, end=' '); print(3,4) #한줄로 출력이 된다.

#출력시키는 문자 사이에 구분자 넣기
print(1,2,3,4,5)
print(1,2,3,4,5,sep=', ')
# file = f 로 파일객체를 전달해서 파일에 값들을 출력할 수 있다.

#서식 출력
print (format(1.234567, '10.3f'))  #10자리를 확보하고, 소수점 이하 3자리 까지(고정소수점)

import math

if __name__ == '__main__':
    for k in range(10):
        print ('sqrt({0})={1:5.3f}'.format(k,math.sqrt(k)))

#복잡한 경우의 출력은 pprint를 이용 할 수 있다
import pprint
complicated = ['asd',(1,2,3),[4,5,6,7,[8,9]]]*3
print(complicated,'\n\n')
pprint.pprint(complicated)
