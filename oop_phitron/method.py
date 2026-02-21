def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 9000
    color = 'red'
    brand = 'rashh'
    feature = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and messages: {sms}'
        return text


my_phone = Phone()

print(my_phone.feature)
my_phone.call()
print(my_phone.send_sms(23456, 'hello rash'))
