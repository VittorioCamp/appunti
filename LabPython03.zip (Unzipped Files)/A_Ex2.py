def A_Ex2(s1,s2):
    if s1=='' or s2=='':
        return 0
    caru=''
    cont=0
    maxlen=min(len(s1),len(s2))
    for i in range(maxlen):
        if s1.count(s1[i]) == s2.count(s2[i]):
            cont+=1
            print(cont,s1[i],s2[i])
    return cont
        
        
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, ['caso palese','casa blue'],4)
    counter_test_positivi += tester_fun(A_Ex2, ['caso palese','casata blue'],3)
    counter_test_positivi += tester_fun(A_Ex2, ['caso palese','casacca blue sole'],3)
    counter_test_positivi += tester_fun(A_Ex2, ['','casa blue'],0)
    counter_test_positivi += tester_fun(A_Ex2, ['',''],0)

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
