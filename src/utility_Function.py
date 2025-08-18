from typing import List
from Card import Card, OffSpell, Potion, DefenseSpell, Weapon
from Player import Player
from Enemy import Enemy
import json
import os
BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'cards.json')
JSON_PATHEnemies = os.path.join(BASE_DIR, '..', 'data', 'enemies.json')

def play(player: Player, card: Card, enemy: Enemy):
    print(f"Playing card: {card}")
    #Player Turn Logic
    if player.mana >= card.cost:
        if isinstance(card, OffSpell):    
            print(f"Dealing {card.damage} damage with {card.name}.")
            enemy.hp -= card.damage
            player.mana -= card.cost           
        elif isinstance(card, DefenseSpell):
            player.hp += card.heal
            print(f"Healing {card.heal} HP with {card.name}.")
            player.mana -= card.cost          
        elif isinstance(card, Potion):
            player.mana += card.manaIncrease
            player.hp += card.heal
            print(f"Healing {card.heal} HP and increasing mana by {card.manaIncrease} with {card.name}.")
            player.mana -= card.cost    
        elif isinstance(card, Weapon):
            player.equipmentmultiplier = card.damagemultiplier
            player.damage = 3 * player.equipmentmultiplier
            player.mana -= card.cost            
        else:
            print(f"Unknown card type: {card.__class__.__name__}")   
    else:
        print (f"Not enogh mana to play {card.name}. Current mana: {player.mana}, card cost: {card.cost}")
        return
    #Enemy Turn Logic
    if enemy.hp > 0:
        enemy.attack(player)
        
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
                cost=0,  
                description=potion['desc'],
                heal=potion['hp_heal'],
                manaIncrease=potion['mana_heal'],
                damage=potion['dmg']
            ))

    # Load weapons
    for entry in data.get('weapons', []):
        for _, weapon in entry.items():
            deck.append(Weapon(
                name=weapon['name'],
                cost=weapon['cost'],
                description=weapon['desc'],
                damagemultiplier=weapon['dmg_amp']
            ))

    # Load attacks as OffSpells
    for entry in data.get('attacks', []):
        for _, attack in entry.items():
            deck.append(OffSpell(
                name=attack['name'],
                cost=attack['cost'],
                description=attack['desc'],
                damage=attack['dmg']
            ))

    return deck


def load_enemy_by_name(name: str) -> Enemy:
    with open(JSON_PATHEnemies, 'r') as file:
        data = json.load(file)

    for enemy_data in data["enemy_deck"]:
        if enemy_data["name"].lower() == name.lower():
            # Convert each card in the JSON to a Card object
            cards = []
            allCards = load_Deck(JSON_PATH)
            
            for card_entry in enemy_data["cards"]:
              for _, card_name in card_entry.items():
                # Find the card in the allCards list
                matching_card = next((c for c in allCards if c.name.lower() == card_name.lower()), None)
                if matching_card:
                    cards.append(matching_card)

            return Enemy(
                hp=enemy_data["health"],
                equipmentmultiplier=1.0,
                hand=cards,  
                mana=1,
                name=enemy_data["name"],
                description=f"Attack: {enemy_data['attack']}, Defense: {enemy_data['defense']}"
            )

    raise ValueError(f"Enemy '{name}' not found in enemies.json")


def draw_card(deck: List[Card]) -> Card:
    if not deck:
        raise ValueError("Deck is empty, cannot draw a card.")
    return deck.pop(0)  # Draw the top card from the deck


    