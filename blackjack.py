from random import randint

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_total = 0

while game_continue:
    game_num += 1
    print(f'START GAME #{game_num}\n')

    player_hand = 0
    card = randint(1, 13)
    if card == 1:
        print('Your card is an ACE!')
    elif 2 <= card <= 10:
        print(f'Your card is a {card}!')
    elif card == 11:
        print('Your card is a JACK!')
        card = 10
    elif card == 12:
        print('Your card is a QUEEN!')
        card = 10
    elif card == 13:
        print('Your card is a KING!')
        card = 10

    player_hand += card
    print(f'Your hand is: {player_hand}\n')

    no_winner = True
    while no_winner:
        print('1. Get another card')
        print('2. Hold hand')
        print('3. Print statistics')
        print('4. Exit\n')
        choice = int(input('Choose an option: '))

        if choice == 1:
            card = randint(1, 13)
            if card == 1:
                print('Your card is an ACE!')
            elif 2 <= card <= 10:
                print(f'Your card is a {card}!')
            elif card == 11:
                print('Your card is a JACK!')
                card = 10
            elif card == 12:
                print('Your card is a QUEEN!')
                card = 10
            elif card == 13:
                print('Your card is a KING!')
                card = 10

            player_hand += card
            print(f'Your hand is: {player_hand}\n')

            if player_hand == 21:
                print('BLACKJACK! You win!\n')
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print('You exceeded 21! You lose.\n')
                dealer_wins += 1
                no_winner = False

        elif choice == 2:
            dealer_hand = randint(16, 26)
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}\n")

            if dealer_hand > 21 or dealer_hand < player_hand:
                print('You win!\n')
                player_wins += 1
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!\n")
                tie_total += 1
            elif dealer_hand > player_hand:
                print('Dealer wins!\n')
                dealer_wins += 1

            no_winner = False
        elif choice == 3:
            print(f'Number of Player wins: {player_wins}')
            print(f'Number of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {tie_total}')
            print(f'Total # of games played is: {game_num - 1}')
            print(f'Percentage of player wins: {float((player_wins / (game_num - 1)) * 100)}%\n')
        elif choice == 4:
            no_winner = False
            game_continue = False
        else:
            print('Invalid input!')
            print('Please enter an integer value between 1 and 4.\n')
