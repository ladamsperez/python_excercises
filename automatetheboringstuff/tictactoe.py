game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def win(current_game):
    for row in game:
        #how might we check all items in this row? We could do something like:
        column_1 = row[0]
        column_2 = row[0]
        column_3 = row[0]
        if column_1 == column_2 == column_3:
            print("WINNER!")
win(game)

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False
        
game = game_board(game_board, player=1, row=3, column=1)

# game_board(game)
# game_board(game, player = 2, row = 0, column = 0)

# print(game)
# https://pythonprogramming.net/mutability-learn-python-3-tutorials/?completed=/function-parameters-learn-python-3-tutorials/
# HELP
# print(id(game))
