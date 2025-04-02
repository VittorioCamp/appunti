def isIntero(s):
    #if s==s.isdecimal():
    if s=='':
        return 'Riprova'
    if (s[0]=='+' or s[0]=='-'):
            for i in s:
                if i!='.':
                    return 'ok'
    elif s.isdecimal():
        for i in s:
            if i!='.':
                return 'ok'
            
    else:
        return 'Riprova'
        
x=input()
y= isIntero(x)
print(y)