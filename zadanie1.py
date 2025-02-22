from kalkulator import kalkulator
from przegladarka_plikow import przegladarka

while 1:
    print("pętla główna")
    polecenie=input()
    match polecenie:
        case 'quit':
            print("wyjście z programu")
            break  
        case 'calc':
            print('tryb kalkulatora')
            kalkulator()
        case 'files':
            print('Przeglądarka plików')
            przegladarka()

    