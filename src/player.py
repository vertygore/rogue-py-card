from typing import List, Optional
from Card import Card, OffSpell, Potion, DefenseSpell, Weapon

class Player:
    def __init__(self, hp: int, equipmentdmg: int = 0, hand: Optional[List[Card]] = None, mana: int = 0):
        self.hp = hp
        self.mana = mana 
        self.hand = hand if hand is not None else []
    def turn(self, chosenCard: isinstance(Card)):
        Card.play(self, chosenCard)
        