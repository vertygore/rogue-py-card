class card:
    def __init__(self, name: str, cost: int, hp: int, damage:int, description: str,type: str):
        self.name = name
        self.cost = cost
        self.hp = hp
        self.damage = damage
        self.description = description
        self.type = type

    def __repr__(self):
        return f"Card(name={self.name}, cost={self.cost}, description={self.description})"

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}) - {self.description}"
    cards = [
        card("Fireball", 3, 0, 5, "Deal 5 damage to a target.", "spell"),
        card("Shield", 2, 5, 0, "Gain 5 HP.", "defensespell"),
        card("Sword", 1, 0, 3, "Deal 3 damage to a target.", "weapon"),
        card("Healing Potion", 2, 0, 0, "Restore 5  HP.", "potion"),
        card("Lightning Bolt", 4, 0, 7, "Deal 7 damage to a target.", "spell"),
        card("Axe", 3, 0, 4, "Deal 4 damage to a target.", "weapon"),
        card("Armor", 2, 10, 0, "Gain 10 HP.", "defensespell"),
        card("Fire Staff", 5, 0, 10, "Deal 10 damage to a target.", "weapon"),
        card("Mana Potion", 1, 0, 0, "Gain 5 mana.", "potion")]