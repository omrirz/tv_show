import pytest


def test_character_favorite_phrase():
    from tv_show import Character
    character = Character()
    assert character.favorite_phrase == ""


def test_character_print(capsys):
    from tv_show import Character
    character = Character()
    character.speak()
    captured = capsys.readouterr()
    assert captured.out == "Character: \n"
