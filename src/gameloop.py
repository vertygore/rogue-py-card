from src.Utility_Function import Utility_Function
from src.Player import Player
from src.Enemy import Enemy
import os

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'cards.json')


class GameLoop():
    def __init__(self):
        enemy = Enemy(name="Goblin", hp=30, description="Green and mean")
        player = Player(hp=100, equipmentmultiplier=1.0, hand=None, mana=1)
        playerdeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
        enemydeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
        while True:
            while len(player.hand) < 5 and playerdeck:
                player.hand.append(Utility_Function.draw_card(playerdeck))

            if not playerdeck:
                print("You have no more cards in your deck!")

            while len(enemy.hand) < 5 and enemydeck:
                enemy.hand.append(Utility_Function.draw_card(enemydeck))

            if not enemydeck:
                print("The enemy has no more cards in their deck!")
            chosenCard = player.hand[0]  # TODO: Chosen card from UI implementation
            Utility_Function.play(player, chosenCard, enemy)
            player.hand.remove(chosenCard)  # Remove the played card from hand	
            enemyCard = enemy.attack(player)
            if enemyCard and enemyCard in enemy.hand:
                enemy.hand.remove(enemyCard)
                
            if enemy.hp <= 0:
                print("You defeated the enemy!")
                break
            if player.hp <= 0:
                print("You were defeated by the enemy!")
                break
            print(f"Enemy HP: {enemy.hp}, Player HP: {player.hp}")
            