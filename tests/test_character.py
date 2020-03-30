import pytest


def test_character_favorite_phrase():
    from tv_show import Character
    character = Character()
    assert character.favorite_phrase == ''


def test_character_print(capsys):
    from tv_show import Character
    character = Character()
    character.speak()
    captured = capsys.readouterr()
    assert captured.out == 'Character: \n'


def test_inherit_character(capsys):
    from tv_show import Character

    class Bender(Character):
        def __init__(self):
            super().__init__(favorite_phrase='Bite my shiny, metal ass!')

    bender = Bender()
    assert bender.favorite_phrase == 'Bite my shiny, metal ass!'
    bender.speak()
    captured = capsys.readouterr()
    assert captured.out == 'Bender: Bite my shiny, metal ass!\n'
