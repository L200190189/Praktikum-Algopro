def konversisuhu(C = 'n', F = 'n'):
    if C == 'n' and F == 'n':
        print('Suhu 0 Celcius setara dengan 32 Fahrenheit')
    elif F == 'n':
        C1 = C * 9 / 5 + 32
        C2 = int(C1)
        print('Suhu', C, 'Celcius setara dengan', C1, 'Fahrenheit')
    elif C == 'n':
        F1 = (F - 32) * 5 / 9
        F2 = int(F1)
        print('Suhu', F, 'Fahrenheit serara dengan', F1, 'Celcius')
