# TV Show

An Example python package

## Installation

```console
# from Pypi
pip install tv_show

# from our gerrit server
pip install git+ssh://ilherldcnjhzl9r:29418/tv_show

# from a wheel file
pip install tv_show-0.0.1-py3.none-any.whl

# from github
pip install git+https://github.com/omrirz/tv_show.git'
```

---

## Usage

```python
from tv_show import Character

character = Character()
character.speak()  # 'Character: '
character.joke()  # Some random joke

# define a new character
class Bender(Character):
    def __init__(self):
        super().__init__(favorite_phrase='Bite my shiny metal ass!')

bender = Bender()
bender.speak()  # 'Bender: Bite my shiny metal ass!'
bender.joke()  # Some random joke
```

---

## Development

```console
pip install -r requirements.txt
```

---

## Test

```console
python -m pytest
```

---

## Build

### 1. To be installed in another project from Gerrit or Git

Nothing to do.

```console
pip install git+ssh://ilherldcnjhzl9r:29418/tv_show
```

### 2. To be installed in another project from local Wheel file

Dependencies:

```console
pip install --upgrade setuptools wheel
```

Then, every time you wish to build the package run:

```console
python setup.py sdist bdist_wheel
```

After that step you will have .whl file in dist dir which can be installed in any other python package by:

```console
pip install tv_show-0.0.1-py3.none-any.whl
```

### 3. To be installed in another project from Pypi

 Follow this guide, it's really easy!
 [packaging-projects](https://packaging.python.org/tutorials/packaging-projects/)
