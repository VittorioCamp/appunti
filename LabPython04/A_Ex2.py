def A_Ex2(s):
    s2=''
    for i in s:
        t=ord(i)
        if t>100:
           s2+=i
           return s2
    else:
        return ''
           

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 3

    counter_test_positivi += tester_fun(A_Ex2, ['CONTE'], '')
    counter_test_positivi += tester_fun(A_Ex2, ['abaco'], 'o')
    counter_test_positivi += tester_fun(A_Ex2, ['adamo'], 'm')

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
