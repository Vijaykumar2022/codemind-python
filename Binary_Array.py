n=int(input())

lst=list(map(int, input().split()))
flag=1
for i in lst:
     if i>1 or i<0:
        flag=0
        break

if flag:
 print("True")
else:
 print("False")