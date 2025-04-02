def A_Ex6(s):
    if len(s)==0:
        return 0
    c=0
    r=''
    for i in s:
        if i.isupper():
            r+=i
            c=r.count(i)
            #c+=1
            print(r,c)
    return c
        
        
        ###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['aHa^^&^HH'], 3)
    counter_test_positivi += tester_fun(A_Ex6, [''], 0)
    counter_test_positivi += tester_fun(A_Ex6, ['&&YH&Y'], 2)
    counter_test_positivi += tester_fun(A_Ex6, ['stri%$p'], 0)
    counter_test_positivi += tester_fun(A_Ex6, ['CIAO'], 1)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

###############################################################################

