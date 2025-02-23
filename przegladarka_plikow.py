import os


def przegladarka():
    while 1:
        user_input = input()  # urzytkownik dejiniuje zmienną przypomocy danych wpisywanych z  klawiatury
        polecenie = user_input.split()  # zmienna dzieli nam zmienną wporwadzoną przez urzytkownika
        current_dir = os.getcwd()  # sprawdza w jakim obecnie katalogu znajduje się urzytkownik

        if polecenie[0] == "q":
            break

        if polecenie[0] == "ls":  # określamy niewiadomą któa jest elementem zerowym tablicy
            dir_list = os.listdir(current_dir)  # określamy niewiadomoą  fukcją która uzyskuje nam pliki i katalogi
            print("Files and directories in '", current_dir, "' :")
            print(dir_list)

        if polecenie[0] == "cd":  # określamy niewiadomą która jest zerowym elementem w tablicy
            try:
                os.chdir(current_dir + '\\' + polecenie[1])  # ta lijnijka przemieszcza urzytkownika z obencego katalogu do katalogu znajdującego sie w obecnym katalogu
            except FileNotFoundError:
                print('Katalog nie istnieje')
            except NotADirectoryError:
                print('Nie można przejść do pliku')

        if polecenie[0] == 'pwd':  # wywołuję sicerzkę w jakiej się znajduje urzytkownik
            print(current_dir)

        if polecenie[0] == 'head':
            try:
                file = open(user_input[5:], 'r', encoding="utf-8")  # niewiadoma otwiera plik do oczytu wybrany przez uzytkownika
                podglad_bajtow = file.read(512)  # niewiadoma otwiera niewiadomą wybraną do odczytu przez urzytkownika i zczytuje pierwsze 512 bajtó
                print(podglad_bajtow)  # fukcja wyswietla piewrsze 512 bajtów pliku wybranego przez urzytkownika
            except FileNotFoundError:
                print('Plik nie istnieje')
            except PermissionError:
                print('Błąd dostepu-czy brubujesz wykonać operację na folderze?')
