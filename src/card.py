from abc import ABC, abstractmethod
# This file defines the Card class and its subclasses for a card game.
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
    def __init__(self, name: str, cost: int, description: str, heal: int, manaIncrease: int, damage: int):
        super().__init__(name, cost, description)
        self.heal = heal
        self.manaIncrease = manaIncrease
        self.damage = damage

class Weapon(Card):
    def __init__(self, name: str, cost: int, description: str, damagemultiplier: float):
        super().__init__(name, cost, description)
        self.damagemultiplier = damagemultiplier
        
