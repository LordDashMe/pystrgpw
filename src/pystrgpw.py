import random


class Generator():

    length = 0
    text = ''
    random_characters = (
        '0123456789abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '~@#$%^&*()_+-=[];,./}{:"|<>?\\'
        "'"
    )

    def length(self, length):
        self.length = length

    def generate(self):
        for x in range(self.length):
            random_index = random.randint(0, len(self.random_characters) - 1)
            self.text += self.random_characters[random_index]

    def get(self):
        return self.text
