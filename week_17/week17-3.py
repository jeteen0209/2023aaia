# SOIT107_Base_010
a = int(input())
days = [0, 31,28,31,30,31,30,31, 31,30,31,30,31]

print( days[a], end='' )


# SOIT107_Base_011
a, c, b = input().split()
a = int(a)
b = int(b)
if c=='+': ans = a+b
if c=='-': ans = a-b
if c=='*': ans = a*b
if c=='/': ans = a//b
print(ans, end='')


c = input()
if c>='A' and c<='Z': ans = 'U'
elif c>='a' and c<='z': ans = 'L'
elif c>='0' and c<='9': ans = 'D'
else: ans = 'O'
print( ans, end='')


# SOIT107_Base_013
a = int(input())

print( (a-1)%7 , end=''