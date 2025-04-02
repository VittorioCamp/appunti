s1=input()
s2=input()
s3=''
if len(s1)<len(s2):
    for t in len(s2):
    s1=s1.app(' ')
if len(s1)==len(s2):
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            s3+=s1[i]
        #s3=s1.replace(s1[i],'')
    print(s3)