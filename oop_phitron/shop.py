class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mayeda = Shop('mayeda begum')
mayeda.add_to_cart('dress')
mayeda.add_to_cart('phone')

print(mayeda.cart)

rasidul = Shop('rash')
rasidul.add_to_cart('laptop')
rasidul.add_to_cart('phone')
print(rasidul.cart)