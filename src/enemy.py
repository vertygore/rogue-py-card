from typing import List, Optional
from Card import Card
from Player import Player


class Enemy:
    def __init__(self, name: str, hp: int, damage: int, description: str, hand:Optional[List[Card]] = None):
        self.hand = hand if hand is not None else []
        self.name = name
        self.hp = hp
        self.damage = damage
        self.description = description

    def attack(self, player: Player):
        player.hp -= self.attack
        print(f"{self.name} attacks for {self.attack} damage! Player HP: {player.hp}")
    def __str__(self):

        return f"{self.name} (HP: {self.hp}, Attack: {self.attack}) - {self.description}"
