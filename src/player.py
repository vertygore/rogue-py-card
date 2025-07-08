from typing import List, Optional
from Card import Card, OffSpell, Potion, DefenseSpell, Weapon
from Utility_Function import play
from Enemy import Enemy

class Player:
    def __init__(self, hp: int, equipmentdmg: int = 0, hand: Optional[List[Card]] = None, mana: int = 0):
        self.hp = hp
        self.mana = mana 
        self.hand = hand if hand is not None else []
    def turn(self, chosenCard: Card, enemy: Enemy):
        play(self, chosenCard, enemy)
        