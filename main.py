#simple noughts and crosses game

move = 1

def print_board():
    for col in board:
        for r in col:
            print(r.ljust(3), end='')
        print()

def input_validation(x, y):
    if x not in ('0', '1', '2') or y not in ('0', '1', '2'):
        print('Вы ввели координаты вне игрового поля')
        return False
    elif board[int(x) + 1][int(y) + 1] != '-':
            print('Поле уже занято. Сходите на другое поле')
            return False
    else:
        print('Ваш ход принят')
        return True

def check_win():
    for i in range(1, 4):
        if all([board[i][j] == 'X' for j in range(1, 4)]) or all([board[i][j] == '0' for j in range(1, 4)]):
            return True
        elif all([board[j][i] == 'X' for j in range(1, 4)]) or all([board[j][i] == '0' for j in range(1, 4)]):
            return True
    if all([board[i][i] == 'X' for i in range(1, 4)]) or all([board[i][i] == '0' for i in range(1, 4)]):
        return True
    elif all([board[i][-i] == 'X' for i in range(1, 4)]) or all([board[i][-i] == '0' for i in range(1, 4)]):
        return True
    return False

#create a game board

board = [['-' for _ in range(4)] for _ in range(4)]

for i in range(3):
    board[0][i + 1] = str(i)
    board[i + 1][0] = str(i)

board[0][0] = ''

print_board()

print('Начало игры.')


if check_win():
    print(f"Поздравляем! {('Крестики', 'Нолики')[move % 2]} победили!")

while True:
    if move % 2:
        print('Ходят крестики')
    else:
        print('Ходят нолики')
    x = input('Укажите координаты по вертикали в числах от 0 до 2: ')
    y = input('Укажите координаты по горизонтали в числах от 0 до 2: ')

    if input_validation(x, y):
        board[int(x) + 1][int(y) + 1] = ('0', 'X')[move % 2]
        print_board()
        move += 1

    if check_win():
        print(f"Поздравляем! {('Крестики', 'Нолики')[move % 2]} победили!")
        break

    if move == 10:
        print('Ничья.')
        break
