def A_Ex1(s):
    if s=='':
        return''
    maxf=0
    c=''
    for i in s:
        f=s.count(i)
        if f>maxf:
            maxf=f
            c=i
        elif f==maxf and i not in c:
            c+=i
            
            print(c)
    return(c)

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, ['caso palese'] ,'ase')
    counter_test_positivi += tester_fun(A_Ex1, ['caso palesemente'] ,'e')
    counter_test_positivi += tester_fun(A_Ex1, ['caso palese zitto'] ,'aso et')
    counter_test_positivi += tester_fun(A_Ex1, ['aca'] ,'a')
    counter_test_positivi += tester_fun(A_Ex1, [''] ,'')

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
