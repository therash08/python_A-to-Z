class phone:
    manufactured = 'china'

    def __init__(self,brand,price, owner):
        self.owner = owner
        self.brand = brand
        self.price = price


    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)


my_phone = phone('rash', '120000', 'therash')
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = phone('she', 'iphone', 200000)
print(her_phone.owner, her_phone.brand, her_phone.price)