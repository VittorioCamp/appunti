def A_Ex4(filename,anno):
    fin=open(filename,'r',encoding='UTF-8')
    anni=fin.readline()
    anni=anni.strip().split(',')
    a=anni.index(str(anno))
    prodotti=fin.readlines()
    cont=0
    for i in prodotti:
        dati=i.strip().split(',')
        maxd=dati[a]
        if int(maxd)>int(cont):
            cont=maxd
        if cont==maxd:
            r=dati[0]
    fin.close()
    return r

        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
