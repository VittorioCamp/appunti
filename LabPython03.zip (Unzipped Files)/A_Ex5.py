def A_Ex5(s):
    if '-' not in s:
        return int(s)
    
    c=0
    s=s.split('-')
    for i in s:
        if i!='-'and int(i)>c: 
            print(c)
            c=int(i)
    return c

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['12-123-45-6-78'] ,123)
    counter_test_positivi += tester_fun(A_Ex5, ['11-12-12'] ,12)
    counter_test_positivi += tester_fun(A_Ex5, ['80-40-80-40'] ,80)
    counter_test_positivi += tester_fun(A_Ex5, ['10'] ,10)
    counter_test_positivi += tester_fun(A_Ex5, ['1-2-3-4-5'] ,5)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)



