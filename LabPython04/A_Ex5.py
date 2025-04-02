def A_Ex5(s):
    n=1
    s1=''
    for i in range(len(s)):
        if s.count(s[i])>=n:
            n=s.count(s[i])
            s1+=s[i]
        s2=s1[-1]
        print(s2,s1)
    return s2

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 4
    
    counter_test_positivi += tester_fun(A_Ex5, ["pippo"], "p")
    counter_test_positivi += tester_fun(A_Ex5, ["clarabella"],"a")
    counter_test_positivi += tester_fun(A_Ex5, ["mamma"], "m")
    counter_test_positivi += tester_fun(A_Ex5, ["cannolo"], "o")
    
    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
