一、
a = int(input())

if a==0: print(0)
if a==1: print(1)
if a==10: print(2)
if a==11: print(3)
if a==100: print(4)
if a==101: print(5)
if a==110: print(6)
if a==111: print(7)
if a==1000: print(8)
if a==1001: print(9)
if a==1010: print(10)
if a==1011: print(11)
if a==1100: print(12)
if a==1101: print(13)
if a==1110: print(14)
if a==1111: print(15)

a = input()

二、
a0 = int(a[0])*8
a1 = int(a[1])*4
a2 = int(a[2])*2
a3 = int(a[3])*1
print( a0 + a1 + a2 + a3 )

三、
a = int(input())

b = a%10
c = a//10%10
d = a//100%10
e = a//1000%10

print( b*1 + c*2 + d*4 + e*8)