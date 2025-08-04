import Utility_Function
from Player import Player
from Enemy import Enemy
import os

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'cards.json')


class GameLoop():
    def __init__(self):
        self.enemy = Enemy(name="Goblin", hp=30, description="Green and mean")
        self.player = Player(hp=100, equipmentmultiplier=1.0, hand=[], mana=1)
        self.playerdeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
        self.enemydeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
        #self.refill_hands()
        #self.execute_turn()


    
    def refill_hands(self, deletedCardIndex = None):
        drawn_Cards = []
        # Check if the player has already played a card
        if deletedCardIndex is not None:
            new_card = Utility_Function.draw_card(self.playerdeck)
            if new_card:
                self.player.hand[deletedCardIndex] = new_card
                type(new_card) 
                drawn_Cards.append({"index": deletedCardIndex, "card": new_card})
            else:
                print("You have no more cards in your deck!")
        # Refill player's hand to 5
        while len(self.player.hand) < 5 and self.playerdeck:
            new_card = Utility_Function.draw_card(self.playerdeck)
            if new_card:
                insert_index = len(self.player.hand)
                self.player.hand.append(new_card)
                drawn_Cards.append({"index": insert_index, "card": new_card})

            else:
                print("You have no more cards in your deck!")
                break
        # Refill enemy's hand
        while len(self.enemy.hand) < 5 and self.enemydeck:
            self.enemy.hand.append(Utility_Function.draw_card(self.enemydeck))

            if not self.enemydeck:
                print("The enemy has no more cards in their deck!")

        return drawn_Cards

    def execute_turn(self, chosenCardIndex:int):
        #Check if the player and enemy have cards in their hands
        if not self.player.hand:
            print("You have no cards in your hand!")
            return
        if not self.enemy.hand:
            print("The enemy has no cards in their hand!")
            return
        
        #Player's turn 
        Utility_Function.play(self.player,  self.player.hand[chosenCardIndex], self.enemy)
        self.player.hand[chosenCardIndex] = None  # Remove the played card from hand

        # Enemy's turn to attack
        enemyCard = self.enemy.attack(self.player)
        self.enemy.hand.remove(enemyCard)

        # Refill hands after playing a card and passing the index of the played card to refill_hands
        drawn_cards = self.refill_hands(deletedCardIndex=chosenCardIndex)

        # return the enemy card and the drawn cards
        return {
            "enemycard": enemyCard,
            "drawnCards": drawn_cards
                }