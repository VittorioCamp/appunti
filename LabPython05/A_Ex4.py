def A_Ex4(n):
    n=str(n)
    for i in range(len(n)):
        if int(n[i])%2!=0 :
            return False
            break
        print(n[i])
    return True
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 4

    counter_test_positivi += tester_fun(A_Ex4, [2416],False)
    counter_test_positivi += tester_fun(A_Ex4, [4860],True) 
    counter_test_positivi += tester_fun(A_Ex4, [0],True)
    counter_test_positivi += tester_fun(A_Ex4, [1],False)


    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

    