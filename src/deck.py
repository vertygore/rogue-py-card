from Card import Card, OffSpell, Potion, DefenseSpell, Weapon
import json
from typing import List
import os


def load_Deck(jsonFilePath: str) -> List[Card]:

    with open(jsonFilePath, 'r') as file:
        data = json.load(file)
    deck: List[Card] = []
    
   # Load offensive spells
    for entry in data.get('spells', []):
        for _, spell in entry.items():
            deck.append(OffSpell(
                name=spell['name'],
                cost=spell['cost'],
                description=spell['desc'],
                damage=spell['dmg']
            ))

    # Load defense spells
    for entry in data.get('defense_spells', []):
        for _, spell in entry.items():
            deck.append(DefenseSpell(
                name=spell['name'],
                cost=spell['cost'],
                description=spell['desc'],
                heal=spell['block']
            ))

    # Load potions
    for entry in data.get('potions', []):
        for _, potion in entry.items():
            deck.append(Potion(
                name=potion['name'],
                cost=0,  # You can adjust if potions should cost something
                description=potion['desc'],
                heal=potion['hp_heal'],
                manaIncrease=potion['mana_heal']
            ))

    # Load weapons
    for entry in data.get('weapons', []):
        for _, weapon in entry.items():
            deck.append(Weapon(
                name=weapon['name'],
                cost=weapon['cost'],
                description=weapon['desc'],
                damage=int(weapon['dmg_amp'] * 10)  # or scale as needed
            ))

    # Load attacks as OffSpells (same logic as offensive spells)
    for entry in data.get('attacks', []):
        for _, attack in entry.items():
            deck.append(OffSpell(
                name=attack['name'],
                cost=attack['cost'],
                description=attack['desc'],
                damage=attack['dmg']
            ))

    return deck


BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'cards.json')

deck = load_Deck(os.path.abspath(JSON_PATH))

def draw_card(deck: List[Card]) -> Card:
    if not deck:
        raise ValueError("Deck is empty, cannot draw a card.")
    return deck.pop(0)  # Draw the top card from the deck

if __name__ == "__main__":
    print("Deck loaded with the following cards:")
    for card in deck:   
        print(card)