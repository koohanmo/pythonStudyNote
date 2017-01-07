"""
문자열 관련 정리
파이썬은 기본적으로 다양한 문자열 메서드를 지원한다.
"""

s='Hello'
print (s.upper())
print (s.split())
print (s.find('llo'))
print (s.startswith('He'))
print (s.endswith('lo'))

#문자열 == 시퀀스 자료형, 변경 불가능(Immutable)자료형
s= "ABCDE"
#s[1]='B'   < - TypeError: 'str' object does not support item assignment

#멤버검사
print ('Hi' in 'Hi everyone?')

#길이
print (len("hello?"))

#Str 생성
str1 = "Python is good!\n"
str2 = "This is long str\
containing back slash and new line.\nGood!\n"
str3 = """가나다라
마바사
아자카타파하"""
print(str1,str2,str3,sep="")

#format
print('{} {}'.format(23,2.12345))
print('{0:1.0f}  {1:0.5}  {2}'.format(1.2,2.3,3.4))
print('{:0,d}'.format(12345678912345789))

#인코딩
#= Str => Bytes
str1="Python"
print(str1.encode())
print(str1.encode('utf-8'))     #기본 인코딩 = utf-8 = ASCII문자 사용시 사용
print(str1.encode('utf-16'))    # 16비트 단위로 유니코드를 인코딩
print(str1.encode('utf-32'))
print(str1.encode('cp949'))

#바이트 : 문자열의 지원 메서드 대부분 지원, 바이트와문자열의 직접적인 연산 허용 X
b=b'python'
print(b)
print (b + ' string'.encode())
print (b.decode()+ ' string') #decode = Bytes => Str

#문서 문자열(Documentation String)
#동적으로 도움말을 얻거나 문서화를 자동으로 해주는 기능
#모듈의 시작부분이나, def, class 다음에 나오는 문자열

import os
print(os.__doc__)