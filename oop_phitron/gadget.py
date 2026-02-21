class laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'running laptop: {self.brand}'
    
    def coding(self):
        return f'lurning python and practise'
    
class phone:
    def __init__(self, brand, price, color, duel_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.duel_sim = duel_sim

    def run(self):
        return f'phone tipa tipi kore'
        
    def phone_call(self, number, text):
        return f'sending sms to : {number} with: {text}'
    
class camara :
    def __init__(self, brand, price, color, pixel) ->None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass
    