import random
from art import logo

# 🃏 Deal a random card from the deck
def deal_card():
    """
    Returns a random card.
    11 represents Ace.
    Face cards (J, Q, K) are represented as 10.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# 🧮 Calculate the score of a hand
def calculate_score(cards):
    """
    Calculates the total score of a hand.
    Returns 0 if the hand is a Blackjack.
    Adjusts Ace value from 11 to 1 if score exceeds 21.
    """
    # 🎯 Blackjack condition
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # 🔄 Adjust Ace value if bust
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# ⚖️ Compare final scores and determine the winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "🤝 Draw"
    elif computer_score == 0:
        return "😞 You lose, opponent has Blackjack!"
    elif user_score == 0:
        return "🎉 You win with a Blackjack!"
    elif user_score > 21:
        return "💥 You went over. You lose!"
    elif computer_score > 21:
        return "🔥 Opponent went over. You win!"
    elif user_score > computer_score:
        return "🏆 You win!"
    else:
        return "❌ You lose!"


# ♠️ Main game logic
def play_game():
    print(logo)

    # 🧑 Player and 🤖 Dealer hands
    user_cards = []
    computer_cards = []

    is_game_over = False

    # 🎴 Initial deal (2 cards each)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 🔁 Player turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n🧑 Your cards: {user_cards} | Score: {user_score}")
        print(f"🤖 Dealer's first card: {computer_cards[0]}")

        # 🛑 End conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("👉 Type 'y' to draw another card, 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 🤖 Dealer logic (draw until 17+)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # 🧾 Final results
    print("\n📊 Final Results")
    print(f"🧑 Your final hand: {user_cards} | Final score: {user_score}")
    print(f"🤖 Dealer's final hand: {computer_cards} | Final score: {computer_score}")

    print("\n🎲 Outcome:")
    print(compare(user_score, computer_score))


# 🔄 Game loop
while input("\n🃏 Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()
