def A_Ex6(filename):
    fin = open(filename, 'r', encoding='UTF-8')
    dati = fin.readlines()
    fin.close()

    # Estrai gli anni dall'intestazione del file
    anni = dati[0].strip().split(',')[1:]

    # Inizializza variabili per tracciare l'anno con vendite massime
    anno_massimo = None
    vendite_massime = 0

    for colonna in range(1, len(anni) + 1):
        vendite_anno_corrente = 0

        for riga in dati[1:]:
            valori = riga.strip().split(',')
            vendite_anno_corrente += int(valori[colonna])

        # Aggiorna l'anno con vendite massime se necessario
        if vendite_anno_corrente > vendite_massime or (vendite_anno_corrente == vendite_massime and int(anni[colonna - 1]) > anno_massimo):
            anno_massimo = int(anni[colonna - 1])
            vendite_massime = vendite_anno_corrente

    return anno_massimo
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
