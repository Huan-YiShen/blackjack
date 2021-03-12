## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import time


def main():
    # start the game by dealing two cards to each player ##############
    player = [deal(), deal()]
    player_score = player[0] + player[1]
    dealer = [deal(False), deal(False)]
    dealer_score = dealer[0] + dealer[1]

    playerWin = False
    
    # player plays ####################################################
    print("You are at ", player_score, "=", player)
    again = input("Would you like to draw another card (Y/N)?")

    while(again =='Y' or again =='y'):
        print("It is Your turn:")
        card = deal()
        player.append(card)
        player_score += card 
        player_score, bust = isBust(player_score, player)
        print("     You are at ", player_score, "=", player)
        
        if (isBlackjack(player_score)):
            break
        elif (bust):
            print("     You Busted")
            break
        
        again = input("Would you like to draw another card (Y/N)?")
    
    # dealer plays ####################################################
    print("It is the dealer's turn:")
    print("Dealer is at", dealer_score, "=", dealer)
    player_score, bust = isBust(player_score, player)
    if (not bust):
        while(dealer_score < 17):
            card = deal()
            dealer.append(card)
            dealer_score += card
            dealer_score, bust = isBust(dealer_score, player)
            time.sleep(1)
            print("     Dealer is at", dealer_score, "=", dealer)
            time.sleep(2)

            if (isBlackjack(dealer_score)):
                break
            elif (bust):
                playerWin = True
                print("     Dealer Busted")
                break
            elif (dealer_score > player_score):
                break

    # compare scores at the end #########################################
    time.sleep(2)
    print("You got", player_score, "and the dealer got", dealer_score)
    if(playerWin or (dealer_score<player_score)):
        print("You Won!")
    elif(dealer_score == player_score):
        print("Draw")
    else:
        print("House Won")

    print("Thank You for Playing!")


def deal(show = True):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_drawn = random.choice(cards)
    if (show):
        print("     Drawing card... ")
        time.sleep(1)
        print("     the card drawn is ", card_drawn)
    return int(card_drawn)


def isBlackjack(score):
    if(score == 21):

        return True
    return False


def isBust(score, cardsInHand):
    while(score > 21):
        if(11 in cardsInHand):
            score -= 10
            cardsInHand[cardsInHand.index(11)] = 1
        else:
            return (score, True) 
        
    return (score, False)


if __name__ == "__main__":
    main()
