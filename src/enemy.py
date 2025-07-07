class Enemy:
    def __init__(self, name: str, hp: int, attack: int, description: str):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.description = description

    def attack(self, player):
        player.hp = player.hp - enemy.attack
        
    def defend(self, player):
        self.hp = self.hp - player.attack
        
    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}) - {self.description}"