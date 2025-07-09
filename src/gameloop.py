from Player import Player
from Enemy import Enemy, attack
import os
import Utility_Function
from Card import OffSpell, DefenseSpell, Potion, Weapon

BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'cards.json')




enemy = Enemy("Goblin", 30, 5, "Green and mean")
player = Player(100, 0, 5)
playerdeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
enemydeck = Utility_Function.load_Deck(os.path.abspath(JSON_PATH))
while True:
    while len(player.hand) < 5:
        player.hand.append(Utility_Function.draw_card(playerdeck))
        if (playerdeck == []):
            print("You have no more cards in your deck!")
            break
    
    while len(enemy.hand) < 5:
        enemy.hand.append(Utility_Function.draw_card(enemydeck))
        if (enemydeck == []):
            print("The enemy has no more cards in their deck!")
            break
    chosenCard = player.hand[0]  # TODO: Chosen card from UI implementation
    Utility_Function.play(player, chosenCard, enemy)
    player.hand.pop(chosenCard)  # Remove the played card from hand	
    
    if enemy.hp <= 0:
        print("You defeated the enemy!")
        break
    if player.hp <= 0:
        print("You were defeated by the enemy!")
        break
    print(f"Enemy HP: {enemy.hp}, Player HP: {player.hp}")
    