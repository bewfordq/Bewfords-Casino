import random
import time

def casino_menu():
    print("""
______                __              _       _____           _             
| ___ \\              / _|            | |     /  __ \\         (_)            
| |_/ / _____      _| |_ ___  _ __ __| |___  | /  \\/ __ _ ___ _ _ __   ___  
| ___ \\/ _ \\ \\ /\\ / /  _/ _ \\| '__/ _ / __| | |    / _ / __| | '_ \\ / _ \\ 
| |_/ /  __/\\ V  V /| || (_) | | | (_| \\__ \\ | \\__/\\ (_| \\__ \\ | | | | (_) |
\\____/ \\___| \\_/\\_/ |_| \\___/|_|  \\__,_|___/  \\____/\\__,_|___/_|_| |_|\\___/ 
""")
    print("🎰 =============================== 🎰")
    
    base_pot = 100
    print(f"💰 Your starting pot is {base_pot}. 💰")
    
    while True:
        print("\n🎮 Select an option to play:")
        print("1. 🪙 Coin Flip Game")
        print("2. 🎰 Slot Machine Game")
        print("3. 🃏 Blackjack Game")
        print("4. 🎲 Dice Game")
        print("5. 🎲 Stake Dice Game")
        print("6. 🚪 Exit")
        
        try:
            choice = int(input("👉 Enter the number of your choice: "))
            if choice == 1:
                base_pot = gambling_game(base_pot)
            elif choice == 2:
                base_pot = slot_machine_game(base_pot)
            elif choice == 3:
                base_pot = blackjack_game(base_pot)
            elif choice == 4:
                base_pot = dice_game(base_pot)
            elif choice == 5:
                base_pot = stake_dice_game(base_pot)
            elif choice == 6:
                print("🎉 Thanks for visiting Bewford's Casino! Goodbye! 🎉")
                time.sleep(3)
                break
            else:
                print("❌ Invalid choice. Please select a valid option (1-6).")
        except ValueError:
            print("❌ Please enter a valid number (1-6).")

def get_player_bet(current_pot):
    while True:
        try:
            bet = int(input("💰 How much do you want to bet? "))
            if bet < 0:
                print("❌ Please enter a positive number.")
            elif bet > current_pot:
                print("💸 You don't have enough money to bet that amount.")
            else:
                return bet
        except ValueError:
            print("❌ Please enter a valid number.")

def gambling_game(pot):
    print("🎰 =============================== 🎰")
    print("\n🪙 Welcome to the Coin Flip Game! 🪙")
    print("In this game, you will bet on whether the coin will land on heads or tails.")
    print("If you guess correctly, you double your bet. If you guess wrong, you lose your bet.")
    print(f"💰 Your current pot: {pot}.")
    
    while True:
        print(f"💰 Your current pot: {pot}")
        bet = get_player_bet(pot)
        if bet == 0:
            print("💸 You don't have enough money to bet. Game over! 💸")
            time.sleep(3)
            break
        
        # Get player guess (1 for heads, 2 for tails)
        guess = get_player_guess()
        result = random.choice(['heads', 'tails'])
        print(f"🪙 The result is: {result}")
        
        # Check if the player's guess matches the result
        if (guess == 1 and result == 'heads') or (guess == 2 and result == 'tails'):
            pot += bet
            print(f"🎉 Congratulations! You won. Your pot is now: {pot}")
        else:
            pot -= bet
            print(f"😢 Oops! You lost. Your pot is now: {pot}")
        
        if pot <= 0:
            game_over()
            break
        
        # Ask if the player wants to play again
        play_again = input("🪙 Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("🎮 Returning to the main menu...")
            time.sleep(2)
            break

    return pot

def get_player_guess():
    while True:
        try:
            guess = int(input("🪙 Enter 1 for Heads or 2 for Tails: "))
            if guess == 1 or guess == 2:
                return guess
            else:
                print("❌ Please enter 1 for Heads or 2 for Tails.")
        except ValueError:
            print("❌ Please enter 1 or 2.")

def slot_machine_game(pot):
    print("🎰 =============================== 🎰")
    print("\n🎰 Welcome to the Slot Machine Game! 🎰")
    print("In this game, you'll spin the slots and try to match symbols.")
    print("You can win various amounts depending on how many symbols you match!")
    
    while True:
        print(f"💰 Your current pot: {pot}")
        bet = get_player_bet(pot)
        if bet == 0:
            print("💸 You don't have enough money to bet. Game over! 💸")
            time.sleep(3)
            break
        
        result = [random.choice(['🍒', '🍉', '🍇', '🍊', '🍋', '⭐']) for _ in range(3)]
        print(f"\n🎰 The slot machine shows: {' | '.join(result)} 🎰")
        
        if result[0] == result[1] == result[2]:
            winnings = bet * 10
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            winnings = bet * 3
        else:
            winnings = -bet
        
        pot += winnings
        print(f"💸 You win: {winnings} 💸")
        print(f"💰 Your new pot is: {pot} 💰")
    
         # Ask if the player wants to play again
        play_again = input("🪙 Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("🎮 Returning to the main menu...")
            time.sleep(2)
        
        if pot <= 0:
            game_over()
            break

    return pot

def blackjack_game(pot):
    print("🎰 =============================== 🎰")
    print("\n🃏 Welcome to Blackjack! 🃏")
    print("Try to get as close to 21 as possible without going over.")
    print("Face cards are worth 10, and Aces are worth either 1 or 11.")

    while True:
        print(f"💰 Your current pot: {pot}")
        bet = get_player_bet(pot)
        if bet == 0:
            print("💸 You don't have enough money to bet. Game over! 💸")
            time.sleep(3)
            break

        deck = create_deck()
        player_hand, dealer_hand = deal_initial_cards(deck)

        print(f"🃏 Your hand: {show_hand(player_hand)} (Total: {calculate_hand_total(player_hand)})")
        print(f"🃏 Dealer's hand: {dealer_hand[0]} and [hidden]")

        while True:
            action = input("🃏 Do you want to Hit (h) or Stand (s)? ").lower()
            if action == 'h':
                player_hand.append(deck.pop())
                print(f"🃏 Your hand: {show_hand(player_hand)} (Total: {calculate_hand_total(player_hand)})")
                if calculate_hand_total(player_hand) > 21:
                    print("💥 You busted! Your hand exceeded 21.")
                    pot -= bet
                    break
            elif action == 's':
                break
            else:
                print("❌ Invalid choice. Please enter 'h' to hit or 's' to stand.")

        if calculate_hand_total(player_hand) <= 21:
            print(f"🃏 Dealer's hand: {show_hand(dealer_hand)} (Total: {calculate_hand_total(dealer_hand)})")
            while calculate_hand_total(dealer_hand) < 17:
                print("🃏 Dealer hits.")
                dealer_hand.append(deck.pop())
                print(f"🃏 Dealer's hand: {show_hand(dealer_hand)} (Total: {calculate_hand_total(dealer_hand)})")
                if calculate_hand_total(dealer_hand) > 21:
                    print("🎉 Dealer busted! You win!")
                    pot += bet
                    break

            if calculate_hand_total(dealer_hand) <= 21:
                player_total = calculate_hand_total(player_hand)
                dealer_total = calculate_hand_total(dealer_hand)
                if player_total > dealer_total:
                    print("🎉 You win!")
                    pot += bet
                elif player_total < dealer_total:
                    print("😢 Dealer wins!")
                    pot -= bet
                else:
                    print("🤝 It's a tie!")
        
        # Ask if the player wants to play again
        play_again = input("🪙 Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("🎮 Returning to the main menu...")
            time.sleep(2)
            break
        if pot <= 0:
            game_over()
            

    return pot

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def deal_initial_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

def calculate_hand_total(hand):
    total = 0
    aces = 0
    for card, _ in hand:
        if card in ['Jack', 'Queen', 'King']:
            total += 10
        elif card == 'Ace':
            aces += 1
            total += 11
        else:
            total += int(card)
    
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def show_hand(hand):
    return ', '.join([f"{card} of {suit}" for card, suit in hand])

def dice_game(pot):
    print("🎰 =============================== 🎰")
    print("\n🎲 Welcome to the Dice Game! 🎲")
    print("In this game, you will roll two dice and bet on the outcome.")
    print("You can bet on specific numbers, the sum of the dice, or other outcomes.")
    print(f"💰 Your current pot: {pot}")

    while True:
        print("\n🎮 Select an option:")
        print("1. Bet on a specific number (pays 5x)")
        print("2. Bet on the sum of the dice (pays 3x)")
        print("3. Bet on doubles (pays 10x)")
        print("4. Exit to Casino Menu")

        try:
            choice = int(input("👉 Enter your choice: "))
            if choice == 1:
                pot = bet_on_specific_number(pot)
            elif choice == 2:
                pot = bet_on_sum(pot)
            elif choice == 3:
                pot = bet_on_doubles(pot)
            elif choice == 4:
                break
            else:
                print("❌ Invalid choice. Please select a valid option (1-4).")
        except ValueError:
            print("❌ Please enter a valid number (1-4).")

        # Ask if the player wants to play again
        play_again = input("🪙 Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("🎮 Returning to the main menu...")
            time.sleep(2)
            
        if pot <= 0:
            print("💸 You are out of money! Game over! 💸")
            break

    return pot

def bet_on_specific_number(pot):
    bet = get_player_bet(pot)
    if bet == 0:
        return pot

    number = int(input("🎲 Enter a number (1-6) to bet on: "))
    if number < 1 or number > 6:
        print("❌ Invalid number. Please enter a number between 1 and 6.")
        return pot

    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    print(f"🎲 The dice show: {dice1} and {dice2}")

    if dice1 == number or dice2 == number:
        winnings = bet * 5
        print(f"🎉 You win! Your winnings: {winnings}")
        pot += winnings
    else:
        print("😢 You lose!")
        pot -= bet

    print(f"💰 Your new pot: {pot}")
    return pot

def bet_on_sum(pot):
    bet = get_player_bet(pot)
    if bet == 0:
        return pot

    total = int(input("🎲 Enter the sum (2-12) to bet on: "))
    if total < 2 or total > 12:
        print("❌ Invalid sum. Please enter a number between 2 and 12.")
        return pot

    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    sum_dice = dice1 + dice2
    print(f"🎲 The dice show: {dice1} and {dice2} (Sum: {sum_dice})")

    if sum_dice == total:
        winnings = bet * 3
        print(f"🎉 You win! Your winnings: {winnings}")
        pot += winnings
    else:
        print("😢 You lose!")
        pot -= bet

    print(f"💰 Your new pot: {pot}")
    return pot

def bet_on_doubles(pot):
    bet = get_player_bet(pot)
    if bet == 0:
        return pot

    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    print(f"🎲 The dice show: {dice1} and {dice2}")

    if dice1 == dice2:
        winnings = bet * 10
        print(f"🎉 You win! Your winnings: {winnings}")
        pot += winnings
    else:
        print("😢 You lose!")
        pot -= bet

    print(f"💰 Your new pot: {pot}")
    return pot

def plinko_game(pot):
    print("🎰 =============================== 🎰")
    print("\n🎯 Welcome to Plinko! 🎯")
    print("Drop the ball and see where it lands!")
    print("Different slots have different payouts. 💰")
    
    slots = [0.5, 1, 2, 5, 2, 1, 0.5]
    slot_positions = len(slots)
    
    while True:
        print(f"💰 Your current pot: {pot}")
        bet = get_player_bet(pot)
        if bet == 0:
            print("💸 You don't have enough money to bet. Game over! 💸")
            time.sleep(3)
            break
        
        position = slot_positions // 2
        path = [position]
        
        for _ in range(9):
            move = random.choice([-1, 1])
            position = max(0, min(slot_positions - 1, position + move))
            path.append(position)
        
        print_plinko_board(path, slot_positions)
        
        multiplier = slots[position]
        winnings = int(bet * multiplier)
        
        if multiplier > 1:
            print(f"🎉 Congratulations! You win {winnings}. Your new pot is: {pot + winnings}")
            pot += winnings
        else:
            print(f"😢 Sorry, you only get {winnings}. Your new pot is: {pot - bet + winnings}")
            pot = pot - bet + winnings
        
        if pot <= 0:
            print("💸 You are out of money! Game over! 💸")
            break

    return pot

def print_plinko_board(path, width):
    board_height = 10
    board_width = width
    board = [[' ' for _ in range(board_width)] for _ in range(board_height)]

    for i in range(board_height):
        for j in range(i + 1):
            if j < board_width:
                board[i][j] = 'O'

    for row, pos in enumerate(path):
        if row < board_height:
            board[row][pos] = 'X'

    for row in board:
        print(' '.join(row))

    print('-' * (board_width * 2 - 1))
    print(' '.join(str(i + 1) for i in range(board_width)))
    print(' '.join(f"x{p}" for p in [0.5, 1, 2, 5, 2, 1, 0.5]))

def game_over():
    print("\n💸 You are out of money! 💸")
    print("💥 Game Over! 💥")
    print("1. Try Again")
    print("2. Exit to Casino Menu")
    
    choice = input("👉 Enter your choice: ").strip()
    
    if choice == '1':
        casino_menu()
    elif choice == '2':
        print("🎉 Thanks for playing! Goodbye! 🎉")
        time.sleep(3)
        exit()
    else:
        print("❌ Invalid choice. Exiting.")
        time.sleep(3)
        exit()

def stake_dice_game(pot):
    print("🎰 =============================== 🎰")
    print("\n🎲 Welcome to the Stake Dice Game! 🎲")
    print("In this game, you will bet on the outcome of a dice roll.")
    print("You can choose to bet on the dice being above, below, or equal to a target number.")
    print(f"💰 Your current pot: {pot}")

    while True:
        print(f"\n💰 Your current pot: {pot}")
        bet = get_player_bet(pot)
        if bet == 0:
            print("💸 You don't have enough money to bet. Game over! 💸")
            time.sleep(3)
            break

        # Get player's target number
        target = get_target_number()

        # Get player's bet type (1 for above, 2 for below, 3 for equal)
        print("\n🎲 Choose your bet type:")
        print("1. Above the target")
        print("2. Below the target")
        print("3. Equal to the target")
        bet_type_choice = input("👉 Enter your choice (1/2/3): ").strip()

        if bet_type_choice == "1":
            bet_type = "above"
            win_chance = (100 - target) / 100
            payout_multiplier = 1 / win_chance
        elif bet_type_choice == "2":
            bet_type = "below"
            win_chance = target / 100
            payout_multiplier = 1 / win_chance
        elif bet_type_choice == "3":
            bet_type = "equal"
            win_chance = 1 / 100
            payout_multiplier = 95  # Standard payout for exact match
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            continue

        # Calculate potential profit
        potential_profit = bet * payout_multiplier

        # Show confirmation message
        print("\n🎲 Bet Confirmation:")
        print(f"🎲 You are betting on the dice being {bet_type} {target}.")
        print(f"🎲 Win chance: {win_chance * 100:.2f}%")
        print(f"🎲 Payout multiplier: {payout_multiplier:.2f}x")
        print(f"🎲 Potential profit: {potential_profit:.2f}")

        # Ask for confirmation
        confirm = input("\n🎲 Confirm your bet? (y/n): ").strip().lower()
        if confirm != 'y':
            print("🎲 Bet cancelled. Returning to the main menu...")
            time.sleep(2)
            break

        # Roll the dice
        dice_roll = random.randint(1, 100)
        print(f"\n🎲 The dice rolled: {dice_roll}")

        # Determine if the player wins
        if (bet_type == "above" and dice_roll > target) or \
           (bet_type == "below" and dice_roll < target) or \
           (bet_type == "equal" and dice_roll == target):
            winnings = bet * payout_multiplier
            pot += winnings
            print(f"🎉 You win! Your winnings: {winnings:.2f}")
        else:
            pot -= bet
            print("😢 You lose!")

        print(f"💰 Your new pot: {pot:.2f}")

        # Ask if the player wants to play again
        play_again = input("\n🎲 Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("🎮 Returning to the main menu...")
            time.sleep(2)
            break

    return pot

def get_target_number():
    while True:
        try:
            target = float(input("🎲 Enter a target number between 1 and 99: "))
            if 1 <= target <= 99:
                return target
            else:
                print("❌ Please enter a number between 1 and 99.")
        except ValueError:
            print("❌ Please enter a valid number.")

def get_bet_type():
    while True:
        bet_type = input("🎲 Bet on 'above', 'below', or 'equal' to the target? ").strip().lower()
        if bet_type in ["above", "below", "equal"]:
            return bet_type
        else:
            print("❌ Invalid choice. Please enter 'above', 'below', or 'equal'.")

# Run the casino menu
if __name__ == "__main__":
    casino_menu()