from typing import List, Optional
from src.Card import Card, OffSpell, Weapon, Potion, DefenseSpell
from src.Player import Player


class Enemy:
    def __init__(self, hp: int, equipmentmultiplier: Optional[float] = 1.0, hand: Optional[List[Card]] = None, mana: int = 1, name: str = "Enemy", description: str = ""):
        self.description = description
        self.name = name
        self.equipmentmultiplier = equipmentmultiplier if equipmentmultiplier is not None else 1.0
        self.hp = hp
        self.mana = mana 
        self.hand = hand if hand is not None else []
        self.name = name
        
    def attack(self, player: Player) -> Card:
        best_weapon = None
        best_heal = None
        best_attack = None
        
        for card in self.hand:
            if self.mana >= card.cost:
                # Check for Mana Potion
                if isinstance(card, Potion) and card.manaIncrease > 0:
                    return card
                # Check for potential lethal cards
                elif isinstance(card, (OffSpell, Potion)) :
                    if (player.hp - (self.equipmentmultiplier * card.damage) <= 0):
                        return card
                    # Save best offensive spell
                    if self.mana >= card.cost:
                        if best_attack is None or card.damage > best_attack.damage:
                            best_attack = card
                # Check for best Weapon        
                elif isinstance(card, Weapon):
                    if card.damagemultiplier > self.equipmentmultiplier:
                        best_weapon = card
                elif isinstance(card, (Potion, DefenseSpell)):
                    if self.hp < 10:
                        best_heal = card
                
        # Priority order
        if best_heal:
            self.hp += best_heal.heal
            self.mana -= best_heal.cost
            return best_heal
        if best_weapon:
            self.equipmentmultiplier = best_weapon.damagemultiplier
            self.mana -= best_weapon.cost
            return best_weapon
        if best_attack:
            player.hp -= (self.equipmentmultiplier * best_attack.damage)
            self.mana -= best_attack.cost
            return best_attack
        else:
            return None
             

        
        
                