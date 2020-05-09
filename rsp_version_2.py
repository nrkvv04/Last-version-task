def game_with_bot():
    gun = ['камень', 'ножницы','бумага']
    player = input('камень,ножницы,бумага: ')
    player_score = 0
    bot_score = 0
    win = 0
    
    #рандомизация инструмента бота
    random = set(gun)
    bot = list(random)
    
    random = set(bot)
    bot = list(random)

    botgun = bot[1]


    print ('Бот выбрал ' +botgun)

    #Условия победы
    if player == 'камень':
        if botgun == 'ножницы':
            player_score += 1
            print ('You won')
    if player == 'ножницы':
        if botgun =='бумага':
            player_score += 1
            print ('You won')
    if player == 'бумага':
        if botgun =='камень':
            player_score += 1
            print ('You won')
    #Условия поражения
    if player == 'камень':
        if botgun == 'бумага':
            bot_score += 1
            print ('You lose')
    if player == 'ножницы':
        if botgun =='камень':
            bot_score += 1
            print ('You lose')
    if player == 'бумага':
        if botgun =='ножницы':
            bot_score += 1
            print ('You lose')
    #Условия ничьи
    if player == botgun:
        print ('Ничья')
    #Условие 3х очковой победы
    if bot_score == 3:
        print ('АБСОЛЮТНЫЙ ПРОИГРЫШ')
    if player_score == 3:
        print ('АБСОЛЮТНАЯ ПОБЕДА')

        
def game_with_player():
    while True:
        player = input('Игрок1: камень,ножницы,бумага: ')
        player2 = input('Игрок2: камень,ножницы,бумага: ')
        player_score = 3
        player2_score = 3
        win = 0
        
        #Условия победы
        if player == 'камень':
            
            if player2 == 'ножницы':
                player_score -= 1
                print ('Игрок 1 выиграл')

        if player == 'ножницы':
            if player2 =='бумага':
                player_score -= 1
                print ('Игрок 1 выиграл')

            
        if player == 'бумага':
            if player2 =='камень':
                player_score -= 1
                print ('Игрок 1 выиграл')
                
           #Условия поражения
        if player == 'камень':
            if player2 == 'бумага':
                player2_score -= 1
                print ('Игрок 2 выиграл')

        if player == 'ножницы':
            if player2 =='камень':
                player2_score -= 1
                print ('Игрок 2 выиграл')

                
        if player == 'бумага':
            if player2 =='ножницы':
                player2_score -= 1
                print ('Игрок 2 выиграл')


        #Условия ничьи
        if player == player2:
            print ('Ничья')

        #Условия 3х очковой победы # НЕ работает :(
        if player_score == win:
            print ('Игрок 1 одержал победу')
            break
        if player2_score == win:
            print ('Игрок 2 одержал победу')
            break
    
gamemode = input('Выбери режим 1- один игрок, 2- два игрока ')
if gamemode == '1':
    game_with_bot()
if gamemode == '2':
    game_with_player()
