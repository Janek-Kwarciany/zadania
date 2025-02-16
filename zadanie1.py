from kalkulator import kalkulator

while 1:
    print("pętla główna")
    polecenie=input()
    if polecenie=="quit":
        print("wyjście z programu")
        break    
    if polecenie=="calc":
        print('tryb kalkulatora')
        kalkulator()
    if polecenie=='files':
        print('Przeglądarka plików')

    