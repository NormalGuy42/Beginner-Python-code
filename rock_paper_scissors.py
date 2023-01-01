import random
import time

def play_RockPaperScissors():
    #Introductions
    player_name = input('Hello player what is your name: ')
    print(f'Nice to meet you {player_name}, let\'s play now')
    time.sleep(0.4)
    print('Game starting...\nYou have 3 tries')
    print("\nYou can input 'Q' to quit")

    #Scores and number of attempts
    tries = 1
    player_score = 0
    comp_score = 0

    #tries is set to less than four because I want the games to go from 1-3
    while tries < 4:
        if player_score == 2 or comp_score == 2:
            break
        
        #Creates line break
        print("___"*30)
        #Prints Game number
        print(f'\nGame number {tries}')
        print(f'Player: {player_score}   Computer:{comp_score}')
        time.sleep(0.5)
        #Asks for input which is then set to uppercase
        u_input = input('Enter rock (r),paper(p) or scisssors(s):').upper()
        time.sleep(0.5)
        
        #If the player puts Q they exit the code
        if u_input == 'Q':
            print(f"Oh {player_name} you're leaving already? Too bad maybe next time")
            exit()
        
        #Available choices
        choices = ['R','P','S']
        comp_input = random.choice(choices)
        
        print(f'\n{player_name} picked {u_input}')
        if u_input in choices: #Only prints the  computer pick when the player pick is valid
            print(f'\nComputer picked {comp_input}')
        

        #Game logic
        if u_input == 'P' and comp_input == 'R'or u_input == 'R' and comp_input == 'S' or u_input == 'S' and comp_input == 'P':
            print(f'\n{player_name} won')
            time.sleep(1)
            player_score += 1
        elif u_input == comp_input:
            print('\nIt\'s a tie')
            time.sleep(1)
        elif u_input not in choices:
            print('\nInvalid Input')
            time.sleep(0.5)
            print('Let\'s try again')
            tries -=1
        else:
            print('\nYou lost')
            time.sleep(1)
            comp_score += 1
        tries += 1
    #If the player wins
    print("___"*30)
    if player_score > comp_score and player_score >1: 
        print(f'\nYay {player_name} you won {player_score} times')
    elif player_score > comp_score and player_score <1:
        print(f'\nYay {player_name} you won 1 time')
    
    #If the computer wins
    if comp_score > player_score and comp_score >1:
        print(f'\nDamn {player_name} you lost, the computer won {comp_score} times')
    elif comp_score > player_score and comp_score <1:
        print(f'\nDamn {player_name} you lost, the computer won 1 time')
   
   #Tie
    if comp_score == player_score:
        print('Incredible it\'s a tie')

play_RockPaperScissors()



