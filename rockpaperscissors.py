import random

def choice_option():
    user_choice = input('Choose rock / paper / scissors: ')
    if user_choice in ['Rock', 'rock', 'R', 'r']:
        user_choice = 'r'
    elif user_choice in ['Paper', 'paper', 'P', 'p']:
        user_choice = 'p'
    elif user_choice in ['Scissors', 'scissors', 'S', 's']:
        user_choice = 's'
    else:
        print('Please choose a valid option!')
        choice_option()
    return user_choice

def computer_choice():
    my_choices = ['r', 'p', 's']
    comp_choice = random.choice(my_choices)
    return comp_choice

user_wins = 0
comp_wins = 0

while True:
    user_choice = choice_option()
    comp_choice = computer_choice()

    if user_choice == 'r' and comp_choice == 'r':
        print('You chose rock. The computer chose rock, too. It\'s a draw!')
        print('')
    
    elif user_choice == 'r' and comp_choice == 'p':
        print('You chose rock. The computer chose paper. You lose!')
        print('')
        comp_wins += 1

    elif user_choice == 'r' and comp_choice == 's':
        print('You chose rock. The computer chose scissors. You win!')
        print('')
        user_wins += 1

    elif user_choice == 'p' and comp_choice == 'r':
        print('You chose paper. The computer chose rock. You win!')
        print('')
        user_wins += 1

    elif user_choice == 'p' and comp_choice == 'p':
        print('You chose paper. The computer chose paper, too. It\'s a draw!')
        print('')

    elif user_choice == 'p' and comp_choice == 's':
        print('You chose paper. The computer chose scissors. You lose!')
        print('')
        comp_wins += 1

    elif user_choice == 's' and comp_choice == 'r':
        print('You chose scissors. The computer chose rock. You lose!')
        print('')
        comp_wins += 1

    elif user_choice == 's' and comp_choice == 'p':
        print('You chose scissors. The computer chose paper. You win!')
        print('')
        user_wins += 1

    elif user_choice == 's' and comp_choice == 's':
        print('You chose scissors. The computer chose scissors, too. It\'s a draw!')
        print('')
    
    print('The computer has won ' + str(comp_wins) + ' times.')
    print('')
    print('You have won ' + str(user_wins) + ' times.')
    print('')
    if comp_wins > user_wins:
        print('So far, the computer is winning!')
        print('')
    elif comp_wins == user_wins:
        print('The jury is still out, keep trying!')
        print('')
    else:
        print('Well done, you are smashing it!')
        print('')
    
    again = input('Would you like to play again? (Y/N)')

    if again in ('Yes', 'yes', 'Y', 'y'):
        pass
    else:
        print('')
        print('Final results: ')
        print('')
        if comp_wins > user_wins:
            print('How unlucky... You\'ve lost.')
        elif comp_wins == user_wins:
            print('You are as smart as a machine!')
        else:
            print('Excellent job - you\'ve beaten the machine!')
        break