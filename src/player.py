from typing import List, Optional
from Card import Card, OffSpell, Potion, DefenseSpell, Weapon
from Utility_Function import play
from Enemy import Enemy

class Player:
    def __init__(self, hp: int, equipmentmultiplier: Optional[float] = 1.0, hand: Optional[List[Card]] = None, mana: int = 0):
        self.equipmentmultiplier = equipmentmultiplier if equipmentmultiplier is not None else 1.0
        self.damage = 3 * equipmentmultiplier
        self.hp = hp
        self.mana = mana 
        self.hand = hand if hand is not None else []
        