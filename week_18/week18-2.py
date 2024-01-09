# SOIT106_BASE_011
a , b = list(map(int, input().split() ))
if a<b: ans = -1
if a==b: ans = 0
if a>b: ans = 1 
print(ans)


# SOIT106_BASE_012
a = int(input())
if a >=90: ans = 'A'
elif 80<=a<90: ans = 'B'
elif 60<=a<80: ans = 'C'
else: ans = 'F'
print(ans)



# SOIT108_BASE_006
a = int(input())
 
if a%400==0: asn = 1
elif a%100==0: ans = 0
elif a%4==0: ans = 1
else: ans = 0 

if ans==1: print(a, 'is a leap year.')
else: print(a, 'is not a leap year.')