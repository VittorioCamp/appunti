n1=int(input())
n2=int(input())
if n1<=0 or n2<=0:
    print('numeri non Naturali')
if n1>n2:
    print('i primo numero deve essere più piccolo del secondo')
for i in range(n1,n2,n1):
        print(i)