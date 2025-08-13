import Utility_Function
from Player import Player
from Enemy import Enemy
import os

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'cards.json')
JSON_PATHEnemies = os.path.join(BASE_DIR, '..', 'data', 'enemies.json')


class GameLoop():
    def __init__(self, enemyName: str):
        self.enemy = Utility_Function.load_enemy_by_name(enemyName)
        self.player = Player(hp=100, equipmentmultiplier=1.0, hand=[], mana=1)
        self.playerdeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
        self.enemydeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATHEnemies))
        self.winner = None
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

            elif not self.playerdeck:
                print("You have no more cards in your deck!")
                break

        return drawn_Cards

    def execute_turn(self, chosenCardIndex:int):
        
        if self.player.hp <= 0:
            print("You have lost the game!")
            self.winner = False
            return
        if self.enemy.hp <= 0:
            print("You have won the game!")
            self.winner = True
            return
        
                   
        if not self.playerdeck:
            print("You have no cards in your Deck left!")
            self.winner = False
            return 
        
        #Player's turn 
        Utility_Function.play(self.player,  self.player.hand[chosenCardIndex], self.enemy)
        self.player.hand[chosenCardIndex] = None  # Remove the played card from hand

        # Enemy's turn to attack
        enemyCard = self.enemy.attack(self.player)

        # Refill hands after playing a card and passing the index of the played card to refill_hands
        drawn_cards = self.refill_hands(deletedCardIndex=chosenCardIndex)

        # return the enemy card and the drawn cards
        return {
            "enemycard": enemyCard,
            "drawnCards": drawn_cards
                }
       