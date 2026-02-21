
import gadget


class device:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        def run(self):
            return f'running laptop: {self.brand}'


class laptop:
    def __init__(self, memory) -> None:

        self.memory = memory

    
    def coding(self):
        return f'lurning python and practise'
    
class phone(gadget):
    def __init__(self, duel_sim) -> None:
        self.duel_sim = duel_sim
        super().__init__(br)

        
    def phone_call(self, number, text):
        return f'sending sms to : {number} with: {text}'
    
    def __repr__(self)  -> str:
        return f'phone:{self.duel_sim} '
    
class camara :
    def __init__(self, pixel) ->None:
        self.pixel = pixel

    def run(self):
        pass
    
my_phone = phone(True)
print(my_phone.)
print(my_phone)