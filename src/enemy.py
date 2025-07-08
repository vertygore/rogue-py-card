from typing import List, Optional
from Card import Card


class Enemy:
    def __init__(self, name: str, hp: int, attack: int, description: str, hand:Optional[List[Card]] = None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.description = description

    def attack(self, player):
        player.hp = player.hp - self.attack
        
    def defend(self, player):
        self.hp = self.hp - player.equipmentdmg
        
    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack},  - {self.description}"