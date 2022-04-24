import random

def game():
    
    print('Welcome to TIC TAC TOE!')

    score1 = []
    score2 = []
    r1 = random.randint(0,1)
    
    if r1 == 0:
        print('Player 1: Choose X or O')
        while True:
            symbol1 = input()
            symbol1 = symbol1.upper()
            if symbol1 == 'X' or symbol1 == 'O':
                break
            else:
                print('Please enter valid symbol. (X|O)')
        
        if symbol1 == 'X':
            symbol2 ='O'
        elif symbol1 == 'O':
            symbol2 = 'X'
            
    elif r1 == 1:
        print('Player 2: Choose X or O')
        while True:
            symbol2 = input()
            symbol2 = symbol2.upper()
            if symbol2 == 'X' or symbol2 == 'O':
                break
            else:
                print('Please enter valid symbol. (X|O)')
                
        if symbol2 == 'X':
            symbol1 ='O'
        elif symbol2 == 'O':
            symbol1 = 'X'
    
    print('')
    print('Here is how you choose the position in which you want to mark your symbol ->')
    print('7 | 8 | 9')
    print('4 | 5 | 6')
    print('1 | 2 | 3')
    print('')
    
    print('Player 1: Please enter your name.')
    Player1 = input()

    print('Player 2: Please enter your name.')
    Player2 = input()

    mylist = ['1','2','3','4','5','6','7','8','9']
    drawlist = []

    def game_list():
        
        mylist2 = []

        for num in mylist:
            if num.isnumeric() == True:
                mylist2.append('')
            else:
                mylist2.append(num)

        print('----------')
        print(' ' + mylist2[6] + ' | ' + mylist2[7] + ' | ' + mylist2[8] + ' ')
        print('----------')
        print(' ' + mylist2[3] + ' | ' + mylist2[4] + ' | ' + mylist2[5] + ' ')
        print('----------')
        print(' ' + mylist2[0] + ' | ' + mylist2[1] + ' | ' + mylist2[2] + ' ')
        print('----------')


    def win_condition():
        if mylist[0] == mylist[1] and mylist[1] == mylist[2]:
            return True
        elif mylist[3] == mylist[4] and mylist[4] == mylist[5]:
            return True
        elif mylist[6] == mylist[7] and mylist[7] == mylist[8]:
            return True
        elif mylist[0] == mylist[4] and mylist[4] == mylist[8]:
            return True
        elif mylist[2] == mylist[4] and mylist[4] == mylist[6]:
            return True
        elif mylist[0] == mylist[3] and mylist[3] == mylist[6]:
            return True
        elif mylist[1] == mylist[4] and mylist[4] == mylist[7]:
            return True
        elif mylist[2] == mylist[5] and mylist[5] == mylist[8]:
            return True
        else:
            return False
        

    game_on = "Y"

    while game_on == "Y":

        mylist = ['1','2','3','4','5','6','7','8','9']
        drawlist = []
        r2 = random.randint(0,1)
        print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))

        while win_condition() == False:
            
            if r2 == 1:
            
                print(Player1 + ': ' + 'Your turn.')

                while True:
                    position1 = input()
                    if position1.isnumeric() != True:
                        continue
                    else:
                        position1 = int(position1)
                        position1 = position1 - 1
                        if mylist[position1].isnumeric() == True:
                            mylist[position1] = symbol1
                            drawlist.append(position1)
                            game_list()
                            break
                        else:
                            print('This position is not empty')

                if win_condition() == True:
                    print(Player1 + ': ' + ' wins!')
                    score1.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

                if len(drawlist) == 9:
                    print('Its a draw!')
                    score1.append(1)
                    score2.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

                while win_condition() == False and len(drawlist) != 9:

                    print(Player2 + ': ' + 'Your turn.')

                    while True:
                        position2 = input()
                        if position2.isnumeric() != True:
                            continue
                        else:
                            position2 = int(position2)
                            position2 = position2 - 1
                            if mylist[position2].isnumeric() == True: 
                                mylist[position2] = symbol2
                                drawlist.append(position2)
                                game_list()
                                break
                            else:
                                print('This position is not empty')
                            
                    break

                if win_condition() == True:
                    print(Player2 + ': ' + ' wins!')
                    score2.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

                if len(drawlist) == 9:
                    print('Its a draw!')
                    score1.append(1)
                    score2.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break


            elif r2 == 0:

                print(Player2 + ': ' + 'Your turn.')

                while True:
                    position2 = input()
                    if position2.isnumeric() != True:
                            continue
                    else:
                        position2 = int(position2)
                        position2 = position2 - 1
                        if mylist[position2].isnumeric() == True: 
                            mylist[position2] = symbol2
                            drawlist.append(position2)
                            game_list()
                            break
                        else:
                            print('This position is not empty')

                if win_condition() == True:
                    print(Player2 + ': ' + ' wins!')
                    score2.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

                if len(drawlist) == 9:
                    print('Its a draw!')
                    score1.append(1)
                    score2.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

                while win_condition() == False and len(drawlist) != 9:

                    print(Player1 + ': ' + 'Your turn.')

                    while True:
                        position1 = input()
                        if position1.isnumeric() != True:
                            continue
                        else:
                            position1 = int(position1)
                            position1 = position1 - 1
                            if mylist[position1].isnumeric() == True:
                                mylist[position1] = symbol1
                                drawlist.append(position1)
                                game_list()
                                break
                            else:
                                print('This position is not empty')
                            
                    break

                if win_condition() == True:
                    print(Player1 + ': ' + ' wins!')
                    score1.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

                if len(drawlist) == 9:
                    print('Its a draw!')
                    score1.append(1)
                    score2.append(1)
                    print('Current score - ' + Player1 + ': ' + str(len(score1)) + ', ' + Player2 + ': ' + str(len(score2)))
                    print('Play again? (Y|N)')
                    game_on_check = input()
                    game_on = game_on_check.upper()
                    break

game()