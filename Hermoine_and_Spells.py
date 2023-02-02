
a,b,c =map(int,input().split())
if b>a and c>a:
    print(b+c)
elif a>b and c>b:
    print(a+c)
elif b>c and a>c:
    print(b+a)