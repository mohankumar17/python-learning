categories = [
    {
        "type": "A",
        "rate": 20
    },
    {
        "type": "B",
        "rate": 15
    },
    {
        "type": "C",
        "rate": 10
    }
]

def getIntrestRate(category):
    return list(filter(lambda cat : cat.get("type") == category, categories))[0].get("rate")

class SimpleIntrest:
    def __init__(self, rate) -> None:
        self.rate = rate
    
    def getSimpleIntrest(self, amount, tenure):
        return (amount * self.rate * tenure)/100
