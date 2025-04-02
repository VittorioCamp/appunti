def A_Ex5(filename,oggetto):
    fin=open(filename,'r',encoding='UTF-8')
    anni=fin.readline()
    oggett=anni.strip().split(',')
    prodotti=fin.readlines()
    print(oggett)
    for i in prodotti:
        dati=i.strip().split(',')
        print(dati)
        for j in range(1,len(dati)):
            continue
        #if oggetto in dati:
            #print(dati[j],j)
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
