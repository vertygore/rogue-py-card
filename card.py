
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, description: str):
        self.name = name
        self.cost = cost
        self.description = description
        
class offspell(Card):
        def __init__(self, damage: int):
            super().__init__(name, cost, description)
            self.damage = damage
        
class defensespell(Card):
        def __init__(self, heal: int):
            super().__init__(name, cost, description)
            self.heal = heal
            
class potion (Card):
        def __init__(self, heal: int):
            super().__init__(name, cost, description)
            self.heal = heal
class weapon(Card):
    def __init__(self, damage: int):
        super().__init__(name, cost, description)
        self.damage = damage
       
    def __repr__(self):
        return f"Card(name={self.name}, cost={self.cost}, description={self.description})"

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}) - {self.description}"
    