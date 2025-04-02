n=int(input())
d=int(input())
if n<d:
    print('la frazzione è propria')
if d%n==0:
    print('la frazzione è apparente')
if n>d and not n%d==0:
    print('la frazzione è improria')