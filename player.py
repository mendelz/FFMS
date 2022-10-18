import random

class player():
    def __init__(self, position, opportunities):
        self.position = position
        self.opportunities = opportunities
    
    def calculate_stats(self):
        if self.position == 'wr':
            receptions = random.randint(1+self.opportunities, 14)
            yards = random.randint(1+self.opportunities, 10*self.opportunities)
        return {"receptions":receptions, "yards":yards}