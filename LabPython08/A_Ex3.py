def A_Ex3(fileName):
    fin=open(fileName,'r',encoding='UTF-8')
    dati=fin.readline()
    dati=fin.readlines()
    res=set()
    w=[]
    c=0
    for i in dati:
        dati=i.strip().split(',')
        if int(dati[1])>=29:
            c+=1
            w.append(dati[2])
            for q in w:
                t=w.count(q)
            if c>=2 and t>=2:
                res.add(dati[2])
    fin.close()
    return res
            
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)