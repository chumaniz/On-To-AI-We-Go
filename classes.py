# Constructing a phone class
class phone():

    amount_phones = 0

    def __init__(self, name, model, country):
        self.name = name
        self.model = model 
        self.country = country

        phone.amount_phones += 1

    def print_info(self):
        print("Name: {}, Model: {}, Country: {}"
              .format(
                  self.name,
                  self.model,
                  self.country
              ))

    def print_phone_amount(self):
        print("Amount: {}".format(phone.amount_phones))

    def __del__(self):
        phone.amount_phones -= 1


        
myphone = phone("iPhone", 12, "America")
myphone.print_info()
myphone.print_phone_amount()

