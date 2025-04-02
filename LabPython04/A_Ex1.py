def A_Ex1(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return ''
    minl=min(len(s1),len(s2))
    s3=''
    i = 0
    while i < minl and s1[i] == s2[i]:
       s3 += s1[i]
       i += 1
    return s3

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, ['amaca','amaranto'], 'ama')
    counter_test_positivi += tester_fun(A_Ex1, ['asso','assolato'], 'asso')
    counter_test_positivi += tester_fun(A_Ex1, ['','stringa'], '')
    counter_test_positivi += tester_fun(A_Ex1, ['stringa',''], '')
    counter_test_positivi += tester_fun(A_Ex1, ['ciao mamma','ciao '], 'ciao ')

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
