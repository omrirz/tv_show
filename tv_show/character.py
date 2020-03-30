import pyjokes


class Character:
    """ Common Character functionalities """
    def __init__(self, favorite_phrase=''):
        self.favorite_phrase = favorite_phrase

    def speak(self):
        """ Prints the name of the character and its favorite phrase """
        print(f"{self.__class__.__name__}: {self.favorite_phrase}")

    def joke(self):
        """ Prints the name of the character and a random joke """
        print(f"{self.__class__.__name__} joke:\n{pyjokes.get_joke()}")
