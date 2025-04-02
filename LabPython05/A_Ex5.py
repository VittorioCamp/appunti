def A_Ex5(n):
    if n<2:
        return 'ERRORE'
    q=''
    for i in range(n*n):
        for j in range(n*n):
            if (i+j)%2!=0:
                q+=( '\n')
            else:
                q+=(' *')
        return q
                
       

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, [2],' *\n* \n')
    counter_test_positivi += tester_fun(A_Ex5, [3],' * \n* *\n * \n') 
    counter_test_positivi += tester_fun(A_Ex5, [4],' * *\n* * \n * *\n* * \n') 
    counter_test_positivi += tester_fun(A_Ex5, [0],'ERRORE')
    counter_test_positivi += tester_fun(A_Ex5, [-1],'ERRORE')

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

    
