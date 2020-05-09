def textcounter():
    strings = 0
    words = 0
    letters = 0
     

    for string in open('text.txt', 'r'):    
        strings += 1
        letters += len(string)
        pos = 'out'
        for letter in string:
            if letter != ' ' and pos == 'out':
                words += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'
    print("Строки:", strings)
    print("Слова:", words)
    print("Буквы:", letters)
textcounter()
