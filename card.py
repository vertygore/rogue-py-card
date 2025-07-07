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
    