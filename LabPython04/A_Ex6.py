def A_Ex6(s1,s2):  #somma due numeri in CP2
    if len(s1)!=len(s2):
        return 'ERRORE'
    
    s3=''
    rip=0
    for i in range(len(s1),-1):
        som=s1[i]+s2[i]+rip
        if som=='0':
            s3+='0'
            rip=0
        elif som=='1':
            s3+='1'
            rip=0
        elif som=='2':
            s3+='0'
            rip=1
        elif som=='3':
            s3+='1'
            rip=1
    if rip==1:
        s3+='1'
      
    if len(s3) > 0 and s3[0] == '1' and len(s3) > len(s1):
            return 'ERRORE'

    else:
        return s3
            
            
        
        
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
if __name__ == '__main__':
    from tester import tester_fun
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['00','01'], '01')
    counter_test_positivi += tester_fun(A_Ex6, ['001','001'], '010')
    counter_test_positivi += tester_fun(A_Ex6, ['010','010'], 'ERRORE')
    counter_test_positivi += tester_fun(A_Ex6, ['00','010'], 'ERRORE')
    counter_test_positivi += tester_fun(A_Ex6, ['000','10'], 'ERRORE')

 
    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
    
