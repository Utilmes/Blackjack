#%%

import classes.classes as classes

Deck = classes.Deck()
Deck.shuffle()

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place your bet."))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("You have not enough funds")
            else:
                break

def hit(deck, player):
    player.add_card(deck.deal_one())
    if player.value > 21:
        player.adjust_for_ace()

def hit_or_stand(deck, player):
    global playing
    while True:
        answer = input("Would you like to hit or stand? Enter 'h' for hit and 's' for stand.")
        if answer[0].lower() == "h":
            hit(deck, player)
            show_some(Thomas, Dealer)
            if player.value > 21:
                print("Player exceeded 21, he is out!")
                playing = False
                break
        elif answer[0].lower() == "s":
            print("Player stands, dealer's turn.")
            playing = False
            break
        else:
            print("I couldn't get the answer try again.")
            continue
        

def dealers_hit(deck, dealer):
    while dealer.value < 17:
        dealer.add_card(deck.deal_one())
        if dealer.value > 21:
            dealer.adjust_for_ace()


def show_some(player, dealer):
    print("\nPlayer cards are: ")
    for card in player.cards:
        print(card)
    print(f"Players value is: {player.value}")

    print("\nDealer cards are: ")
    print(dealer.cards[1])

def show_all(player, dealer):
    print("\nPlayer cards are: ", *player.cards, sep="\n")
    print(f"The value for the player's hand is {player.value}")

    print("\nDealer cards are: ", *dealer.cards, sep="\n")
    print(f"The value for the dealer's hand is {dealer.value}")


def player_busts(player, chips):
    print(f"Player busted as his cards sum {player.value}")
    chips.lose_bet()

def player_wins(player, chips):
    print(f"Player won! He added up {player.value}")
    chips.win_bet()

def dealer_busts(player, chips):
    print(f"Player won, dealer busted! He added up {player.value}")
    chips.win_bet()

def dealer_wins(dealer, chips):
    print(f"Dealer Won, he added up {dealer.value}")
    chips.lose_bet()
    
def push():
    print("Dealer and player tie!")

def continue_playing():
    while True:
        answer = input("Would you like to play? y or n")
        if answer[0].lower() == "y" or answer[0].lower() == "n":
            break
        else:
            print("Please enter y or n.")
    if answer[0].lower() == "y":
        return True
    elif answer[0].lower() == "n":
        return False
    
def restart():
    Thomas.cards = []
    Thomas.value = 0
    Dealer.cards = []
    Dealer.value = 0
    


Thomas = classes.Player("Thomas")
Dealer = classes.Player("Dealer")

ThomasChips = classes.Chips(1000)

game_on = True

while game_on:
    game_on = continue_playing()
    if game_on == False:
        break
    #Take initial bet
    take_bet(ThomasChips)

    restart()
    
    for x in range(2):
        Thomas.add_card(Deck.deal_one())
        Dealer.add_card(Deck.deal_one())
    
    #Show player's and dealer's cards
    show_some(Thomas, Dealer)

    if Thomas.value == 21:
        print("BlackJack! Congratulations, you won!")
        player_wins(Thomas, ThomasChips)
    else:
        #Ask player what he wants to do
        playing = True
        while playing == True:
            hit_or_stand(Deck, Thomas)
        
        dealers_hit(Deck, Dealer)

        show_all(Thomas, Dealer)

        if Thomas.value > 21:
            player_busts(Thomas, ThomasChips)
        elif Dealer.value > 21:
            dealer_busts(Thomas, ThomasChips)
        elif Thomas.value > Dealer.value:
            player_wins(Thomas, ThomasChips)
        elif Thomas.value < Dealer.value:
            dealer_wins(Dealer, ThomasChips)
        else:
            push()





# %%
