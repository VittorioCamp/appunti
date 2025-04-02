a=int(input())
b=int(input())
c=int(input())
if a>0 and b>0 and c>0:
    if a==b and a==c and b==c:
        print('equilatero')
    elif a==b or b==c or c==a:
        print('isoscele')
    else:
        print('scaleno')
else:
    print('input non valido')