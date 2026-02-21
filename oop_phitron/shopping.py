class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    # remove item from cart
    def remove_item(self, item):
        for product in self.cart:
            if product['item'] == item:
                self.cart.remove(product)
                print(f"{item} removed from cart")
                return
        print(f"{item} not found in cart")

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']

        print('total price', total)

        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money: {extra}')


swapan = Shopping('Alan Swapon')

swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice', 50, 5)

print(swapan.cart)

# remove example
swapan.remove_item('dim')

swapan.checkout(1600)
