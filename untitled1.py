import qiskit
from qiskit import *

def options():
    print('What move would you like to make?')
    print('1 - Classical Move')
    print('2 - Superposition Move')
    print('3 - Entanglement')
    print('4 - Measure All')
    
    while True:
        try:
            option = int(input('Enter your choice (1-4): '))
            if 1 <= option <= 4:
                return option
            else:
                print('Invalid input, please try again.')
        except ValueError:
            print('Invalid input, please try again.')
def display_options():
    print('What move would you like to make?')
    print('1 - Classical Move')
    print('2 - Superposition Move')
    print('3 - Entanglement')
    print('4 - Measure All')

def grid():
    grid = {
        '1': [' ', 0], '2': [' ', 0], '3': [' ', 0],
        '4': [' ', 0], '5': [' ', 0], '6': [' ', 0],
        '7': [' ', 0], '8': [' ', 0], '9': [' ', 0]
    }
    return grid

def print_grid(grid):
    print('\n')
    print(f' {grid["1"][0]} | {grid["2"][0]} | {grid["3"][0]} ')
    print('---+---+---')
    print(f' {grid["4"][0]} | {grid["5"][0]} | {grid["6"][0]} ')
    print('---+---+---')
    print(f' {grid["7"][0]} | {grid["8"][0]} | {grid["9"][0]} ')
    print('\n')

def check_win(grid):
    # Check rows
    for i in range(1, 8, 3):
        if grid[str(i)][0] == grid[str(i+1)][0] == grid[str(i+2)][0] != ' ':
            return True

    # Check columns
    for i in range(1, 4):
        if grid[str(i)][0] == grid[str(i+3)][0] == grid[str(i+6)][0] != ' ':
            return True

    # Check diagonals
    if (grid['1'][0] == grid['5'][0] == grid['9'][0] != ' ') or \
       (grid['3'][0] == grid['5'][0] == grid['7'][0] != ' '):
        return True

    return False

def classical_move(turn, grid, qc):
    while True:
        location = input('Pick a location (1-9): ')
        if location in grid and grid[location][0] == ' ':
            grid[location][0] = turn
            # Apply X gate to the corresponding qubit
            qc.x(int(location) - 1)
            break
        else:
            print('Invalid location, please try again.')

def superposition_move(turn, grid,qc):
    while True:
        location1 = input('Pick the first location (1-9): ')
        location2 = input('Pick the second location (1-9): ')
        if location1 in grid and location2 in grid and grid[location1][0] == grid[location2][0] == ' ':
            grid[location1][0] = turn
            grid[location2][0] = turn
            qc.h(int(location1)-1)
            qc.x(int(location2)-1)
            qc.cx(int(location1)-1,int(location2)-1)
            break
        else:
            print('Invalid locations, please try again.')

def start_game(grid):
    turn = 'X'
    winner = False
    counter = 0
    qc = qiskit.QuantumCircuit(9, 9)

    while not winner and counter < 9:
        print_grid(grid)
        
        display_options()  # Display options at the beginning of each turn

        move_option = int(input(f"Player {turn}, choose your move option (1-2): "))

        if move_option == 1:
            classical_move(turn, grid, qc)
        elif move_option == 2:
            superposition_move(turn, grid, qc)
        elif move_option == 3:
            pass  # Entanglement
        elif move_option == 4:
            pass  # Measure All

        counter += 1
        winner = check_win(grid)
        turn = 'O' if turn == 'X' else 'X'

    print_grid(grid)
    print('Quantum Circuit:')
    print(qc)

    if winner:
        print(f'Player {turn} wins!')
    else:
        print("It's a draw!")

grid = grid()
start_game(grid)