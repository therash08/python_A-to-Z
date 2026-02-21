class shop:
    shopping_mall = 'jamuna'
    def __init__(self, buyer):
        self.buyer = buyer

        self.cart =[] # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


mayeda = shop('mayeda begum')
mayeda.add_to_cart('dress')
mayeda.add_to_cart('phone')

print(mayeda.cart)

rasidul = shop('rash')
rasidul.add_to_cart('laptop')
rasidul.add_to_cart('phone')
print(rasidul.cart)