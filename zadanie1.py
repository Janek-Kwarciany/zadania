while 1:
    print("pętla główna")
    polecenie=input()
    if polecenie=="quit":
        print("wyjście z programu")
        break    
    if polecenie=="calc":
        print('tryb kalkulatora')
        while 1:
            print('pętla kalkulatora')
            polecenie_w_trybie_calc=input()
            if polecenie_w_trybie_calc=="q":
                break
            if polecenie_w_trybie_calc=="+":
                print('Wbrano operację dodawania')
                print('podaj liczbę a')
                a=input()
                print('podaj liczbę b')
                b=input()
                c=float(a)+float(b)
                print('wynik')
                print(c)
            if polecenie_w_trybie_calc=='-':
                print('Wbrano operację odejmowanie')
                print('podaj liczbę a')
                a=input()
                print('podaj liczbę b')
                b=input()
                c=float(a)-float(b)
                print('wynik')
                print(c)
            if polecenie_w_trybie_calc=='*':
                print('Wbrano operację mnożenie')
                print('podaj liczbę a')
                a=input()
                print('podaj liczbę b')
                b=input()
                c=float(a)*float(b)
                print('wynik')
                print(c)
            if polecenie_w_trybie_calc=='/':
                print('Wbrano operację dzielenie')
                print('podaj liczbę a')
                a=input()
                print('podaj liczbę b')
                b=input()
                c=float(a)/float(b)
                print('wynik')
                print(c)
            if polecenie_w_trybie_calc=='!':
                print('Wbrano operację silnia') 
                print('podaj liczbę n')
                n=float(input())
                fact=1
                for i in range(1, n+1):
                    print(fact)
                    fact = fact * i
                print('wynik')
                print(fact)
            if polecenie_w_trybie_calc=='^':
                print('Wbrano operację potegowanie') 
                print('podaj liczbę a')
                a=input()
                print('podaj liczbę b')
                b=input()
                c=float(a)**float(b)
                print('wynik')
                print(c)
    if polecenie=='files':
        print('Przeglądarka plików')