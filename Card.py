from abc import ABC, abstractmethod
import Player
import Enemy

class Card(ABC):
    def __init__(self, name: str, cost: int, description: str):
        self.name = name
        self.cost = cost
        self.description = description

    def __repr__(self):
        return f"Card(name={self.name}, cost={self.cost}, description={self.description})"

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}) - {self.description}"

class OffSpell(Card):
    def __init__(self, name: str, cost: int, description: str, damage: int):
        super().__init__(name, cost, description)
        self.damage = damage

class DefenseSpell(Card):
    def __init__(self, name: str, cost: int, description: str, heal: int):
        super().__init__(name, cost, description)
        self.heal = heal

class Potion(Card):
    def __init__(self, name: str, cost: int, description: str, heal: int, manaIncrease: int):
        super().__init__(name, cost, description)
        self.heal = heal
        self.manaIncrease = manaIncrease

class Weapon(Card):
    def __init__(self, name: str, cost: int, description: str, damage: int):
        super().__init__(name, cost, description)
        self.damage = damage
        
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