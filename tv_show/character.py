class Character:
    def __init__(self):
        self.favorite_phrase = ''

    def speak(self):
        print(f"{self.__class__.__name__}: {self.favorite_phrase}")
