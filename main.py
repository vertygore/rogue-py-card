import pygame
import card

"""
GAMENAME_TBD von Daniel Kern und Angelo Walburger

Grundidee:
Kartenspiel + Roguelike, angelehnt an 'Slay The Spire'

Startdeck, Deck kann erweitert werden und wird stärker mit Progess
(Am Ende) Man kann herumlaufen, Begegnungen starten Kämpfe als Kartenspiel

Optionen zum upgraden von Runs:
 - mehr Leben
 - bessere RNG-Chancen
 - Kartenupgrades
 - neue Karten
 - etc.

"""

def main():
    cards = [
        card.card("Fireball", 3, 0, 5, "Deal 5 damage to a target.", "spell"),
        card.card("Shield", 2, 5, 0, "Gain 5 HP.", "defensespell"),
        card.card("Sword", 1, 0, 3, "Deal 3 damage to a target.", "weapon"),
        card.card("Healing Potion", 2, 0, 0, "Restore 5  HP.", "potion"),
        card.card("Lightning Bolt", 4, 0, 7, "Deal 7 damage to a target.", "spell"),
        card.card("Axe", 3, 0, 4, "Deal 4 damage to a target.", "weapon"),
        card.card("Armor", 2, 10, 0, "Gain 10 HP.", "defensespell"),
        card.card("Fire Staff", 5, 0, 10, "Deal 10 damage to a target.", "weapon"),
        card.card("Mana Potion", 1, 0, 0, "Gain 5 mana.", "potion")]
    print("Hello World!")




if __name__ == "__main__":
    main()