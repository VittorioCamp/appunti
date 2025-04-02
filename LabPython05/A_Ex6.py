def A_Ex6(v1,v2):
    d=0
    g=1
    ve=v1
    #v=v2-v1
    #t=
    for i in range(1,v1):
            v2*=i
            d+=v2
            print(v1,v2,g,d)
            if d>=v1:
                break
            v1+=ve
            g+=1
    return g
                    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 4

    counter_test_positivi += tester_fun(A_Ex6, [20,1],39)
    counter_test_positivi += tester_fun(A_Ex6, [10,5],3) 
    counter_test_positivi += tester_fun(A_Ex6, [1,1],1)
    counter_test_positivi += tester_fun(A_Ex6, [100,10],19)


    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

    