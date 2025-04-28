# Monte Carlo Simulator
**Author:** _Daniel Ra_  
**Project Name:** _Monte Carlo Simulator (DS5100)_

---

## Synopsis

This package simulates a Monte Carlo experiment using dice-like objects.  
It allows you to create dice, roll them multiple times, and analyze the results.

### Installation

```bash
pip install montecarlo-simulator
```

### Quick Demo

```python
import numpy as np
from montecarlo.die import Die
from montecarlo.game import Game
from montecarlo.analyzer import Analyzer

# Create a die
faces = np.array(['H', 'T'])
die = Die(faces)

# Play a game
game = Game([die, die, die])  # Three dice
game.play(10)                 # Roll 10 times

# Analyze the game
analyzer = Analyzer(game)
jackpot_count = analyzer.jackpot()
face_counts = analyzer.face_counts_per_roll()
combo_counts = analyzer.combo()
perm_counts = analyzer.permutation()

print(f"Jackpots: {jackpot_count}")
print(face_counts)
print(combo_counts)
print(perm_counts)
```

---

## API Description

### Class: `Die`

> A die has N sides or faces, each with an associated weight. Faces can be strings or numbers. Weights default to 1.0 but can be changed after initialization.

#### Public Methods:
- `__init__(faces: numpy.ndarray)`
  - **Args:** `faces`: NumPy array of distinct face values (numeric or string)
  - **Raises:** TypeError, ValueError

- `change_weight(face, weight)`
  - **Args:** 
    - `face` (str or number): The face to change.
    - `weight` (float or int): New weight.
  - **Raises:** IndexError, TypeError

- `roll(num_rolls=1)`
  - **Args:** `num_rolls` (int, default=1): Number of times to roll.
  - **Returns:** list of outcomes.

- `show()`
  - **Returns:** pandas DataFrame of current faces and weights.

---

### Class: `Game`

> A game consists of rolling one or more dice of the same kind multiple times.

#### Public Methods:
- `__init__(dice: list)`
  - **Args:** `dice`: A list of Die objects.

- `play(num_rolls: int)`
  - **Args:** `num_rolls`: Number of times to roll all dice.

- `show(form='wide')`
  - **Args:** 
    - `form` (str, default='wide'): Return format, either `'wide'` or `'narrow'`.
  - **Returns:** pandas DataFrame with play results.
  - **Raises:** ValueError if form not `'wide'` or `'narrow'`.

---

### Class: `Analyzer`

> An Analyzer object takes the results of a single Game object and computes descriptive statistical properties about it.

#### Public Methods:
- `__init__(game: Game)`
  - **Args:** `game`: An instance of Game.
  - **Raises:** ValueError if input not a Game.

- `jackpot()`
  - **Returns:** Integer count of jackpots (all faces identical).

- `face_counts_per_roll()`
  - **Returns:** pandas DataFrame of face counts per roll.

- `combo()`
  - **Returns:** pandas DataFrame showing distinct combinations of faces rolled and their counts (order-independent).

- `permutation()`
  - **Returns:** pandas DataFrame showing distinct permutations of faces rolled and their counts (order-dependent).
