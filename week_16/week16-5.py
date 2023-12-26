# SOIT108_Advance_014
a = int(input())
ans = 0 
for i in range (1, 2*a+1+1, 2):
	ans += i
print(f'f({a})={ans}', end='')



# SOIT108_Advance_014B
a = int(input())

ten = 1
while a>0:
	now = a%10 * ten
	print(now, end=' ')
	a = a // 10
	ten = ten * 10
