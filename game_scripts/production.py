class Production:
    def __init__(self, game):
        self.game = game

    def food_production(self):
        return self.game.farmer  
    
    def wood_production(self):
        return self.game.woodcutter 
    
    def merchant_production(self):
        return self.game.merchant  
    
    def metal_production(self):
        return self.game.miner  
    
    def knowledge_production(self):
        return self.game.scholar  