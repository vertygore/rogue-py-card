import Player
import Enemy
import Card

enemy = Enemy("Goblin", 30, 5, "Green and mean")
player = Player(100, 0, 5)
while True:
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
    
    