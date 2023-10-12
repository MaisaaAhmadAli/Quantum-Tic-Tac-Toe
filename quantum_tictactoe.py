import qiskit
from qiskit import *
from qiskit_aer import AerSimulator
import sys
from termcolor import colored ,cprint
def choose_mode():
    """
    Prompts the user to choose a game mode for Quantum Tic-Tac-Toe.
    """
    print("Welcome to Quantum Tic-Tac-Toe! \n\n")
    print("Choose a game mode:")
    print("1. Superposition")
    print("2. Entanglement\n\n")
    Entanglement_moves ={
        "Classical": "Occupy 1 empty spot with 100% probability.",
        "Entanglement": "Occupy 1 empty spot and 1 opponent's spot with a 50% probability of being X and 50% probability of being O in each spot.",
        "Measurement": "Collapse all entanglements, leaving only classical spots and valid entanglement moves.",
        "Winning": "Get 3 measured spots in a straight row, column or diagonal line."
        }
    Superposition_moves = {
    "Classical": "Occupy 1 empty spot with 100% probability.\n",
    "Superposition": "Occupy 2 empty spots with 50% probability in each.\n",
    "Measurement": "Collapse all superpositions, leaving only classical spots and valid superposition moves.\n",
    "Winning": "You only win when a row or a column is filled with classical move.\n"
        }


    while True:
        choice = input("Enter your choice (1 or 2):")
        if choice == '1':
            print("You chose: Superposition\n")
               #Prints the types of moves and their descriptions.
            print("Types of moves:\n")
            for i, (key, value) in enumerate(Superposition_moves.items(), start=1):
                 print(f"{i}. {key}: {value}")
            return 1
            break
        elif choice == '2':
            print("You chose: Entanglement")
            #Prints the types of moves and their descriptions.
            print("Types of moves:")
            for i, (key, value) in enumerate(Entanglement_moves.items(), start=1):
                 print(f"{i}. {key}: {value}")
            return 2
            break
        else:
            print("Invalid input. Please enter 1 or 2.")


# Example usage
mood=choose_mode()
if mood==1:
    #Superposition

    def options():
        print('What move would you like to make?')
        print('1 - Classical Move')
        print('2 - Superposition Move')
        print('3 - Measure All')
    
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
        print('3 - Measure All')
    
    def grid():
        """
    Initialize and return the Tic-Tac-Toe grid.

    The grid is represented as a dictionary with keys '1' to '9' corresponding
    to the positions on the Tic-Tac-Toe board. The values are a list containing
    two elements: the symbol ('X', 'O', or ' ') at that position and a flag (0 or 1)
    indicating if the position has been marked or not.

    Returns:
    grid (dict): The Tic-Tac-Toe grid with initial values.
    """
        
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
    
    def check_win(turn, grid,qc):
        """
    Check if there is a winner in the Tic-Tac-Toe game.

    Args:
    turn (str): Current player's turn ('X' or 'O').
    grid (dict): The Tic-Tac-Toe grid representing the game state.
    qc (int): Quantum counter indicating the number of quantum moves made.

    Returns:
    win (bool): True if there is a winner, False otherwise.
    winner (str): Symbol ('X', 'O') of the winner, if any.
    """
        # Check rows
        for i in range(1, 8, 3):
            if grid[str(i)][0] == grid[str(i+1)][0] == grid[str(i+2)][0] != ' ':
                if grid[str(i)][1] == grid[str(i+1)][1] == grid[str(i+2)][1] == 1:
                    winner1=grid[str(i)][0]
                    return True,winner1
    
    
        # Check columns
        for i in range(1, 4):
            if grid[str(i)][0] == grid[str(i+3)][0] == grid[str(i+6)][0] != ' ':
                if grid[str(i)][1] == grid[str(i+3)][1] == grid[str(i+6)][1] ==1:
                    winner1=grid[str(i)][0]
                    return True,winner1
    
        # Check diagonals
        if (grid['1'][0] == grid['5'][0] == grid['9'][0] != ' '):
            if (grid['1'][1] == grid['5'][1] == grid['9'][1] == 1):
                winner1=grid['1'][0]
                return True,winner1
    
        if (grid['3'][0] == grid['5'][0] == grid['7'][0] != ' '):
            if (grid['3'][1] == grid['5'][1] == grid['7'][1] ==1):
                winner1=grid['3'][0]
                return True,winner1
        winner1=' '
    
        return False,winner1
    
    def classical_move(turn, grid, qc):
        while True:
            location = input('Pick a location (1-9): ')
            if location in grid and grid[location][0] == ' ':
                grid[location][0] = turn
                grid[location][1] = 1
                # Apply X gate to the corresponding qubit
                qc.x(int(location) - 1)
                break
            else:
                print('Invalid location, please try again.')
    def superposition_move(turn, grid, qc):
        """
    Perform a superposition move in the Tic-Tac-Toe game.

    Args:
    turn (str): Current player's turn ('X' or 'O').
    grid (dict): The Tic-Tac-Toe grid representing the game state.
    qc (QuantumCircuit): The quantum circuit representing the game.

    The function prompts the current player to pick two locations (1-9) on the grid.
    If the locations are valid, unmarked, and belong to the same player, the function
    updates the grid, applies an H gate to the first location's qubit, and applies a CNOT
    gate from the first location's qubit to the second location's qubit in the quantum circuit.

    Returns:
    None
    """
    
        while True:
            location1 = input('Pick the first location (1-9): ')
            location2 = input('Pick the second location (1-9): ')
            if location1 in grid and location2 in grid and grid[location1][0] == grid[location2][0] == ' ':
                if turn == 'X':
    
                    grid[location1][0] = turn.lower()
                    grid[location2][0] =turn.lower()
                else :
                    grid[location1][0] = turn.lower()
                    grid[location2][0] =turn.lower()
                qc.h(int(location1) - 1)
                qc.x(int(location2) - 1)
                qc.cx(int(location1) - 1, int(location2) - 1)
                break
            else:
                print('Invalid locations, please try again.')
    
    
    
    
    
    def Measurements(turn, grid,qc):
        """
    Perform measurements in the Tic-Tac-Toe game.

    Args:
    turn (str): Current player's turn ('X' or 'O').
    grid (dict): The Tic-Tac-Toe grid representing the game state.
    qc (QuantumCircuit): The quantum circuit representing the game.

    The function performs measurements on the qubits in the quantum circuit. It retrieves
    the measurement results and updates the grid accordingly, marking the positions as 'X',
    'O', or ' ' depending on the measurement outcomes.

    Returns:
    V (int): The number of remaining Planck locations.
    """
        V=9
        l=list(range(9))
    
        qc.measure(l,l)
        output = execute(qc, AerSimulator()).result().get_counts(qc)
        measures=list(output.keys())
        measures1=[]
        for i in measures[0]:
            measures1.append(int(i))
        measures1.reverse()
        for i in range(9):
            grid[str(i+1)][1] = measures1[i]
            if measures1[i]==0:
                grid[str(i+1)][0]=' '
            elif measures1[i]==1:
                grid[str(i+1)][0] = grid[str(i+1)][0].upper()
                V-=1
        return V
    
    
    
    
    def start_game(grid):
        """
    Start the Tic-Tac-Toe game.

    Args:
    grid (dict): The Tic-Tac-Toe grid representing the game state.

    The function initializes the game with the 'X' player's turn and sets the initial winner
    status as False. It creates a quantum circuit with 9 qubits. The function runs a loop that
    continues until there is a winner. In each iteration, it prints the grid, displays the move
    options, prompts the player to choose amove option, and calls the corresponding move function based on the player's choice. It also checks for the number of remaining Planck locations and performs measurements if necessary. Finally, it checks for a winner and updates the turn to the next player.

    Returns:
    None
    """
        turn = 'X'
        winner = False
        PlanckLocations=9
        qc = qiskit.QuantumCircuit(9, 9)
    
        while not winner :
            print_grid(grid)
    
            display_options()  # Display options at the beginning of each turn
    
    
    
            move_option = int(input(f"Player {turn}, choose your move option (1,2,3): "))
    
            if move_option == 1:
                classical_move(turn, grid, qc)
                PlanckLocations-=1
            elif move_option == 2:
                superposition_move(turn, grid, qc)
                PlanckLocations-=2
            elif move_option == 3:
                PlanckLocations=Measurements(turn, grid,qc)
            
    
            if PlanckLocations==0:
                print('no planck locations left! (auto measurements)')
                PlanckLocations=Measurements(turn, grid,qc)
                print(PlanckLocations,'locations left')
                if PlanckLocations==0:
                    winner,player = check_win(turn, grid,qc)
                    if not winner:
                        print("it's a tie !")
    
    
            winner,player = check_win(turn, grid,qc)
            if winner:
                print(f'Player {player} wins!')
            #else:
                #print("It's a draw!")
            turn = 'O' if turn == 'X' else 'X'
    
        print_grid(grid)
        
    
    
    grid = grid()
    start_game(grid)
elif mood==2:
    

    #entangelement game
    
    
    
    
    def display_options():
        print('What move would you like to make?')
        print('1 - Classical Move')
        print('2 - Entanglement Move')
        print('3 - Measure All')
    
    def grid():
        """
    Initialize and return the Tic-Tac-Toe grid.

    The grid is represented as a dictionary with keys '1' to '9' corresponding
    to the positions on the Tic-Tac-Toe board. The values are a list containing
    two elements: the symbol ('X', 'O', or ' ') at that position and a flag (0 ,1 or None)
    indicating if the position has been marked or not.

    Returns:
    grid (dict): The Tic-Tac-Toe grid with initial values.
    """
        grid = {
            '1': [' ', None], '2': [' ', None], '3': [' ', None],
            '4': [' ', None], '5': [' ', None], '6': [' ', None],
            '7': [' ', None], '8': [' ', None], '9': [' ', None]
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
    
    def check_win(turn, grid,qc):
        """
    Check if there is a winner in the Tic-Tac-Toe game.

    Args:
    turn (str): Current player's turn ('X' or 'O').
    grid (dict): The Tic-Tac-Toe grid representing the game state.
    qc (int): Quantum counter indicating the number of quantum moves made.

    Returns:
    win (bool): True if there is a winner, False otherwise.
    winner (str): Symbol ('X', 'O') of the winner, if any.
    """
    # Check rows
        for i in range(1, 8, 3):
            if grid[str(i)][0] == grid[str(i+1)][0] == grid[str(i+2)][0] != ' ':
                if grid[str(i)][1] == grid[str(i+1)][1] == grid[str(i+2)][1] != None:
                    winner1=grid[str(i)][0]
                    return True,winner1
                
        
        # Check columns
        for i in range(1, 4):
            if grid[str(i)][0] == grid[str(i+3)][0] == grid[str(i+6)][0] != ' ':
                if grid[str(i)][1] == grid[str(i+3)][1] == grid[str(i+6)][1] != None:
                    winner1=grid[str(i)][0]
                    return True,winner1
                
        # Check diagonals
        if (grid['1'][0] == grid['5'][0] == grid['9'][0] != ' '):
            if (grid['1'][1] == grid['5'][1] == grid['9'][1] != None): 
                winner1=grid['1'][0]
                return True,winner1
            
        if (grid['3'][0] == grid['5'][0] == grid['7'][0] != ' '):
            if (grid['3'][1] == grid['5'][1] == grid['7'][1] != None):
                winner1=grid['3'][0]
                return True,winner1
        winner1=' '
        
        return False,winner1
    
    def Eclassical_move(turn, grid, qc):
        while True:
            location = input('Pick a location (1-9): ')
            if location in grid and grid[location][0] == ' ':
                grid[location][0] = turn[0]
                grid[location][1] = turn[1]
                # Apply X gate to the corresponding qubit if turn is X otherwise its only 0 by the reset function belwo
                qc.reset(int(location) - 1)
                if turn[0]=='X':
                    qc.x(int(location)-1)
                break
            else:
                print('Invalid location, please try again.')
    
    def entangelement_move(turn, grid,qc):
        """
    Perform a entangelement move in the Tic-Tac-Toe game.

    Args:
    turn (str): Current player's turn ('X' or 'O').
    grid (dict): The Tic-Tac-Toe grid representing the game state.
    qc (QuantumCircuit): The quantum circuit representing the game.

    The function prompts the current player to pick two locations (1-9) on the grid.
    If the locations are valid, one of them is unmarked, and the other location belongs to the opponent, the function
    updates the grid to have the symbole 'XO' to indicated the entangelment,
    applies  reset on all locations , H gate to one location ,
    X gate to the other location,and cx gate betwen them both 

    Returns:
    None
    """
        while True:
            entalgenment_looks='XO'
            location1 = input('Pick the first location (1-9): ')
            location2 = input('Pick the second location (1-9): ')
            
        
            input_correctnes=False
            if (grid[location1][0] ==entalgenment_looks or grid[location2][0] ==entalgenment_looks ):
                while not(input_correctnes):
                    print('Invalid locations, please try again.')
                    location1 = input('Pick the first location (1-9): ')
                    location2 = input('Pick the second location (1-9): ')
        
                    if (grid[location1][0] !=entalgenment_looks and  grid[location2][0] !=entalgenment_looks):
                        input_correctnes=True
            if (location1 in grid or location2 in grid) and (grid[location1][0] ==' 'or grid[location2][0] == ' '):
                if (grid[location1][1]!=None and grid[location2][0]!=turn):
                    grid[location1][0] = entalgenment_looks
                    grid[location2][0] = entalgenment_looks
                    grid[location1][1] = None
                    grid[location2][1] = None
                    qc.barrier()
                    qc.reset(int(location1) - 1)
                    qc.reset(int(location2) - 1)
                    qc.h(int(location1) - 1)
                    qc.x(int(location2) - 1)
                    qc.cx(int(location1)-1,int(location2)-1)
                    break
                elif (grid[location2][1]!=None and grid[location1][0]!=turn):
                    grid[location1][0] = entalgenment_looks
                    grid[location2][0] = entalgenment_looks
                    grid[location1][1] = None
                    grid[location2][1] = None
                    qc.reset(int(location1) - 1)
                    qc.reset(int(location2) - 1)
                    qc.barrier()
                    qc.h(int(location2) - 1)
                    qc.x(int(location1) - 1)
                    qc.cx(int(location2)-1,int(location1)-1)
                    break
            else:
                print('Invalid locations, please try again.')
    
    
    
    def Emeasurement(turn, grid,qc) :
        """
    Perform measurement on the full cells of a grid and update their types.
    
    Args:
        turn (int): Current turn number.
        grid (dict): Dictionary representing the grid.
        qc (QuantumCircuit): Quantum circuit for measurement.
        
    Returns:
        int: Updated count of empty places in the grid.
    """
        Ecount = 9 # Empty places counter 
        Full_empty=[] #list to determin types after Ms
        for i in range (9):
          if grid[str(i+1)][0] == ' ':
            Full_empty.append("E") #empty cell
             #dont measure empty cell
          elif grid[str(i+1)][0]!= ' ':
              Full_empty.append("F") #full cell
              Cbit=ClassicalRegister(1) #creat a Cbit
              qc.add_bits(Cbit) #Append it to the circuit
              qc.measure(i, Cbit) #take measurement on full cell to the Cbit
        
        output = execute(qc, AerSimulator()).result().get_counts(qc)
        
        measures1=list(output.keys()) #list has 1 item:string of the Ms
        measures2=[]
        for i in measures1[0]:
            measures2.append(int(i))
        measures2.reverse() #list has correct order of integer Ms
        d=0
        for j in range(9):
            if Full_empty[j]=="E":
                Full_empty[j]=None #type of the empty cell after Ms
            elif Full_empty[j]=="F":
                Full_empty[j]=measures2[d] #type of full cell after Ms
                d+=1 #for the nixt M result
        
        for i in range(9):
            if Full_empty[i]==1:
                grid[str(i+1)][0]='X'
                grid[str(i+1)][1]=Full_empty[i]
                Ecount -=1
            elif Full_empty[i]==0:
                grid[str(i+1)][0]='O'
                grid[str(i+1)][1]=Full_empty[i]
                Ecount -=1
            elif Full_empty[i]==None:
                grid[str(i+1)][0]=' '
                grid[str(i+1)][1]=Full_empty[i]
                
        
        return Ecount        
           
    
    
    def start_game(grid):
        turn = ['X',1]
        winner = False
        
        Ecount = 9 
        qc = qiskit.QuantumCircuit(9)
        qc.h(list(range(9)))
        
        while not winner :
            print_grid(grid)
            
            display_options()  # Display options at the beginning of each turn
        
            move_option = int(input(f"Player {turn[0]}, choose your move option (1,2,4): "))
        
            if move_option == 1:
                Eclassical_move(turn, grid, qc)
                Ecount -=1
            
            elif move_option == 2:
                entangelement_move(turn, grid,qc) # Entanglement
                Ecount -=1
            elif move_option == 3:
                Ecount =Emeasurement(turn, grid,qc)
            if  Ecount==0:
                print('no planck locations left! (auto measurements)')
                Ecount =Emeasurement(turn, grid,qc)
                print(Ecount,'locations left')
                if Ecount==0:
                    winner,player = check_win(turn, grid,qc)
                    if not winner:
                        print("it's a tie !")
            
            
            
        
            
            winner,player = check_win(turn, grid,qc)
            if winner:
                print(f'Player {player} wins!')
            
            turn = ['O',0] if turn == ['X',1] else ['X',1]
        
        print_grid(grid)
    
    
    
    
    
    grid = grid()
    start_game(grid)

