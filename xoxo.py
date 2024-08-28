b = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
s = 0
p = 0
x_wins = 0
y_wins = 0
draws = 0

def display_board(pos):
    global s
    global p

    if s == 0:
        print(' | ' + b[0] + ' | ' + b[1] + ' | ' + b[2] + ' | ')
        print(' | ' + b[3] + ' | ' + b[4] + ' | ' + b[5] + ' | ')
        print(' | ' + b[6] + ' | ' + b[7] + ' | ' + b[8] + ' | ')
    write_to_file(pos)

def write_to_file(pos):
    global s
    global x_wins
    global y_wins
    global draws
    try:
        with open('MyFile.txt', 'a+') as file:
            if s == 0:
                if p == 1:
                    file.write(f"{p1} Enter Your Position: " + str(pos) + '\n')

                elif p == 2:
                    file.write(f"{p2} Enter Your Position: " + str(pos) + '\n')

                file.write(' | ' + b[0] + ' | ' + b[1] + ' | ' + b[2] + ' | ' + '\n')
                file.write(' | ' + b[3] + ' | ' + b[4] + ' | ' + b[5] + ' | ' + '\n')
                file.write(' | ' + b[6] + ' | ' + b[7] + ' | ' + b[8] + ' | ' + '\n' + '\n')

            if s == 1:
                x_wins += 1
                file.write("Game Over. The Winner is Player X" + '\n' + '\n')
                file.write('Total wins (X): ' + str(x_wins) + '\n' + '\n')
                print("Game Over. The Winner is Player X")
                print('Total wins (X):', x_wins)
                s = 0

            elif s == 2:
                y_wins += 1
                file.write("Game Over. The Winner is Player O" + '\n' + '\n')
                file.write('Total wins (O): ' + str(y_wins) + '\n' + '\n')
                print("Game Over. The Winner is Player O")
                print('Total wins (O):', y_wins)
                s = 0

            elif s == 3:
                draws += 1
                file.write("Game Over. Match Drawn" + '\n' + '\n')
                file.write('Total Drawn: ' + str(draws) + '\n' + '\n')
                print("Game Over. Match Drawn")
                print('Total Drawn:', draws)
                s = 0
    except Exception as e:
        print(f"Error writing to text file: {e}")

p1 = 'X'
p2 = 'O'

def board_full():
    return len([i for i in b if i == '-']) == 0

def check_winner(pl):
    conds = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]
    for c in conds:
        if b[c[0]] == pl and b[c[1]] == pl and b[c[2]] == pl:
            return 1
    return 0

def start_game():
    global s
    display_board(0)
    while True:
        while True:
            try:
                p1_pos = int(input(f"{p1}, Enter Your Position : "))
                if p1_pos not in range(1, 10):
                    print('Please enter [1-9]')
                    continue

                if b[p1_pos - 1] == '-':
                    b[p1_pos - 1] = p1
                    global p
                    p = 1
                    display_board(p1_pos)
                    if check_winner(p1):
                        s = 1
                        display_board(p1_pos)
                        return
                    break
                else:
                    print('This Place is Not Empty')
            except ValueError:
                print("Please enter a valid number")

        if board_full():
            s = 3
            display_board(p1_pos)
            return

        while True:
            try:
                p2_pos = int(input(f"{p2}, Enter Your Position : "))
                p = 2

                if p2_pos not in range(1, 10):
                    print('Please enter [1-9]')
                    continue

                if b[p2_pos - 1] == '-':
                    b[p2_pos - 1] = p2
                    display_board(p2_pos)
                    if check_winner(p2):
                        s = 2
                        display_board(p2_pos)
                        return
                    break
                else:
                    print('This Place is Not Empty')
            except ValueError:
                print("Please enter a valid number")

start_game()

while True:
    play_again = input('Do you want to play again [y/n] : ')
    if play_again.lower() == 'y':
        b = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        start_game()
    elif play_again.lower() == 'n':
        exit()
    else:
        print("Enter a valid input")
