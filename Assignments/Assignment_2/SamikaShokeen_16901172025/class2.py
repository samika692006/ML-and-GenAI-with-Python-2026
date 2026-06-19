import math
def remainder(n,m):
    return n%m
def square_num(n):
    return n**2
def cube_num(n):
    return n**3
def area_rect(l,b):
    return l*b
def area_circle(r):
    return math.pi*r*r
def simple_interest(p,r,t):
    return (p*r*t)/100
def average(n1,n2,n3):
    return (n1+n2+n3)/3
# print(remainder(10,4))
# print(square_num(10))
# print(cube_num(10))
# print(area_circle(10))
# print(area_rect(10,20))
# print (average(3,4,5))
# print(10+5*2)
# for i in range(1,6):
#     for j in range(1,i):
#         print(j,end="")
#     print()

# for i in range(6,0,-1):
#     print("*"*i)
# for i in range(6):
#     print("*"*6)
# # print()
# c=1
# while c<=5:
#     print(c)
#     c+=1


##exercise ##
for i in range(11):
    print(i)
print()
for i in range(2,22,2):
    print(i)
print()
n=3
for i in range(1,11):
    print(n,"*",i,"=",n*i)
print()
n=int(input("enter age"))
if n>=18: print('eligible to vote')
print()

n=int(input("enter the number whose factorial we need to find"))
prod=1
for i in range(1,n+1):
    prod*=i
print(prod)

l=int(input("enter marks"))
if l>=90:
    print("A")
elif l>=80: print("B")
elif l>70: print("C")
else:print("D")
print()
t=input("enter number")
print(t[::-1])
#or 
p=int(input("enter number"))
while p>1:
    print(p%10,end="")
    p=p//10