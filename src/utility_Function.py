from typing import List
from Card import Card, OffSpell, Potion, DefenseSpell, Weapon
from Player import Player
from Enemy import Enemy

def play(player: Player, card: Card, enemy: Enemy):
    print(f"Playing card: {card}")

    if isinstance(card, OffSpell):
        print(f"Dealing {card.damage} damage with {card.name}.")
        enemy.hp -= card.damage
        return
    elif isinstance(card, DefenseSpell):
        player.hp += card.heal
        print(f"Healing {card.heal} HP with {card.name}.")
        return
    elif isinstance(card, Potion):
        player.mana += card.manaIncrease
        player.hp += card.heal
        print(f"Healing {card.heal} HP and increasing mana by {card.manaIncrease} with {card.name}.")
        return
    elif isinstance(card, Weapon):
        player.equipmentdmg = card.damage
        print(f"Increasing equipment damage by {card.damage} with {card.name}.")
        return
    return