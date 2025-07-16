import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from Gameloop import GameLoop
from Card import Card, OffSpell, Weapon, Potion, DefenseSpell

class TestGameLoop(unittest.TestCase):
    def check_subclass_instances(self, drawnCards):
        for card in drawnCards:
            self.assertIsInstance(card, Card)
            self.assertNotEqual(type(card), Card)
            
    def test_pos1(self):
        # This is a placeholder for the first test case
        gameloop = GameLoop()
        result = gameloop.execute_turn(0)
        drawnCards = [item["card"] for item in result["drawnCards"]]
        self.check_subclass_instances(drawnCards)
        pass 

    def test_pos2(self):
        # This is a placeholder for the first test case
        gameloop = GameLoop()
        result = gameloop.execute_turn(1)
        drawnCards = [item["card"] for item in result["drawnCards"]]
        self.check_subclass_instances(drawnCards)
        pass
    
    def test_pos3(self):
        # This is a placeholder for the first test case
        gameloop = GameLoop()
        result = gameloop.execute_turn(2)
        drawnCards = [item["card"] for item in result["drawnCards"]]
        self.check_subclass_instances(drawnCards) 
        pass 

    def test_pos4(self):
        # This is a placeholder for the first test case
        gameloop = GameLoop()
        result = gameloop.execute_turn(3)
        drawnCards = [item["card"] for item in result["drawnCards"]]
        self.check_subclass_instances(drawnCards)
        pass 

    def test_pos5(self):
        # This is a placeholder for the first test case
        gameloop = GameLoop()
        result = gameloop.execute_turn(4)
        drawnCards = [item["card"] for item in result["drawnCards"]]
        self.check_subclass_instances(drawnCards)
        pass 

if __name__ == '__main__':
    unittest.main()