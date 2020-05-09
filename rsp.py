gun = ['камень', 'ножницы','бумага']
player = gun[int(input('0-камень, 1-ножницы, 2-бумага: '))]
player_score = 0
bot_score = 0

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
        player_score = player_score +1
        print ('You won')
if player == 'ножницы':
    if botgun =='бумага':
        player_score = player_score +1
        print ('You won')
if player == 'бумага':
    if botgun =='камень':
        player_score = player_score +1
        print ('You won')
#Условия поражения
if player == 'камень':
    if botgun == 'бумага':
        bot_score = bot_score +1
        print ('You lose')
if player == 'ножницы':
    if botgun =='камень':
        bot_score = bot_score +1
        print ('You lose')
if player == 'бумага':
    if botgun =='ножницы':
        bot_score = bot_score +1
        print ('You lose')
#Условия ничьи
if player == botgun:
    print ('Ничья')
#Условие 3х очковой победы
if bot_score == 3:
    print ('АБСОЛЮТНЫЙ ПРОИГРЫШ')
if player_score == 3:
    print ('АБСОЛЮТНАЯ ПОБЕДА')
