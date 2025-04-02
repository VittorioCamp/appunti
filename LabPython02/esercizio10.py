x=int(input())
y=int(input())
for i in range(0,11):
    if x in [i] or y in [i]:
        continue
    print(i)
        