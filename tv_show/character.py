import pyjokes


class Character:
    def __init__(self, favorite_phrase=''):
        self.favorite_phrase = favorite_phrase

    def speak(self):
        print(f"{self.__class__.__name__}: {self.favorite_phrase}")

    def joke(self):
        print(f"{self.__class__.__name__} joke:\n{pyjokes.get_joke()}")
