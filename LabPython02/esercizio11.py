t=int(input())
car=input()
car=car.upper()
if car=='C':
    if t<=0:
        print('solida')
    if t>0 and t<100:
        print('liquida')
    if t>=100:
        print('gassosa')
elif car=='F':
    t=((t-32)/1.8)
    if t<=0:
        print('solida')
    if t>0 and t<100:
        print('liquida')
    if t>=100:
        print('gassosa')