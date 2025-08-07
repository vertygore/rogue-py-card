
import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import UIManager as uim
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



if __name__ == "__main__":
    
    ui = uim.UIManager()