import Player
import Enemy
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
        Utility_Function.draw_card(playerdeck)
    
    while len(enemy.hand) < 5:
        Utility_Function.draw_card(enemydeck)
        
    player.turn(player.hand[0])  # in a real game, you would choose a card from the player's hand
    
    enemy.attack(player)
    player.attack(enemy)
    if enemy.hp <= 0:
        print("You defeated the enemy!")
        break
    if player.hp <= 0:
        print("You were defeated by the enemy!")
        break
    print(f"Enemy HP: {enemy.hp}, Player HP: {player.hp}")
    
    