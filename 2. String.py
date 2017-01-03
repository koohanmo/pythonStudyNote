"""
파이썬은 기본적으로 다양한 문자열 메서드를 지원한다.
"""

s='Hello'
print (s.upper())
print (s.split())
print (s.find('llo'))
print (s.startswith('He'))
print (s.endswith('lo'))

# 문자열은 변경이 불가능하다.(튜플처럼)
s= "ABCDE"
#s[1]='B'   < - TypeError: 'str' object does not support item assignment

