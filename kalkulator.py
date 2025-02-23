def kalkulator():
    while 1:
        file=open('historia1234', 'a', encoding="utf-8")
        print('pętla kalkulatora')
        polecenie_w_trybie_calc=input()
        if polecenie_w_trybie_calc=="q":
            break

        elif polecenie_w_trybie_calc=="+":
            print('podaj liczbę a')
            a=input()
            print('podaj liczbę b')
            b=input()
            c=int(a)+int(b)
            print('wynik')
            print(c)
            file.write('dodawanie: ' + a + " + " + b)
            file.write('\n')
            file.write("wynik=" + str(c))
            file.write('\n')

        elif polecenie_w_trybie_calc=='-':
            print('podaj liczbę a')
            a=input()
            print('podaj liczbę b')
            b=input()
            c=int(a)-int(b)
            print('wynik')
            print(c)
            file.write('odejmowanie:' + a + "-" + b)
            file.write('\n')
            file.write('wynik=' + str(c))
            file.write('\n')

        elif polecenie_w_trybie_calc=='*':
            print('podaj liczbę a')
            a=input()
            print('podaj liczbę b')
            b=input()
            c=int(a)*int(b)
            print('wynik')
            print(c)
            file.write('mnożenie:' + a + "*" +b)
            file.write('\n')
            file.write('wynik=' + str(c))
            file.write('\n')

        elif polecenie_w_trybie_calc=='/':
            print('podaj liczbę a')
            a=input()
            print('podaj liczbę b')
            b=input()
            try:
                c=int(a)/int(b)
                print('wynik')
                print(c)
                file.write('dzielenie:' + a + "/" +b)
                file.write('\n')
                file.write('wynik=' + str(c))
                file.write('\n')
    
            except ZeroDivisionError:
                print("Nie można podzielić przez 0!")

        elif polecenie_w_trybie_calc=='!':
            print('podaj liczbę n')
            n=int(input())
            if n>0:    
                fact=1
                for i in range(1, n+1):
                    print(fact)
                    fact = fact * i
                print('wynik')
                print(fact)
                file.write("silnia:" + str(n) + "!")
                file.write("\n")
                file.write('wynik=' + str(n))
                file.write("\n")
            else:
                print('Silnia możliwa tylko od liczb >0')

        elif polecenie_w_trybie_calc=='^':
            print('podaj liczbę a')
            a=input()
            print('podaj liczbę b')
            b=input()
            c=int(a)**int(b)
            print('wynik')
            print(c)
            file.write('potegowanie:' + a + '^' +b)
            file.write('\n')
            file.write('wynik=' + str(c))
        else:
            print('Podano nieprawidłowe operacje, możliwe operacje: +, -, *, /, ^, !, q-do wyjścia ')
        file.close()