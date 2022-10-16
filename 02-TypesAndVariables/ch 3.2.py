score = input('Write down score: ')
try:
    if score > 0 and score <= 1.0:
        if float(score) < 0.6:
            print('F')
        elif float(score) >= 0.6 and float(score) < 0.7:
            print('D')
        elif float(score) >= 0.7 and float(score) < 0.8:
            print('C')
        elif float(score) >= 0.8 and float(score) <0.9:
            print('B')
        elif float(score) >= 0.9:
            print('A')
    else:
        print('Bad score')
except:
    print('Bad score')
