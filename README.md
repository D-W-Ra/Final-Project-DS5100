# Monte Carlo Simulator
**Author:** _Daniel Ra_  
**Project Name:** _Monte Carlo Simulator (DS5100)_

---

## Metadata

This project implements a Monte Carlo simulator that can simulate dice rolls (or similar stochastic processes) and analyze the outcomes.  
It consists of three main classes: **Die**, **Game**, and **Analyzer**.

---

## Synopsis

Here is an example of how to install, import, and use the Monte Carlo Simulator:

```bash
pip install -e .
```

```python
# Import necessary classes
import numpy as np
from montecarlo.die import Die
from montecarlo.game import Game
from montecarlo.analyzer import Analyzer

# 1. Create dice
faces = np.array(['H', 'T'])
die1 = Die(faces)
die2 = Die(faces)

# 2. Play a game
game = Game([die1, die2])
game.play(100)

# 3. Analyze the game
analyzer = Analyzer(game)

# Number of jackpots (rolls where all faces match)
jackpot_count = analyzer.jackpot()
print(f"Number of jackpots: {jackpot_count}")

# Face counts per roll
face_counts = analyzer.face_counts_per_roll()
print(face_counts.head())

# Combinations
combo_counts = analyzer.combo()
print(combo_counts.head())

# Permutations
perm_counts = analyzer.permutation()
print(perm_counts.head())
```

---

## API Description

Below is a description of each class, including all public methods and attributes:

---

### Die Class

Represents a single die, which can have arbitrary faces and custom weights.

**Attributes:**
- None publicly accessible.

**Methods:**
- `__init__(faces: np.ndarray)`
  - Initializes the die with faces.
  - **Parameters:**
    - `faces` (numpy.ndarray): An array of distinct face values (strings or numbers).
  - **Raises:**
    - `TypeError` if faces is not a numpy array.
    - `ValueError` if faces are not unique.
  - **Returns:** None.

- `change_weight(face, weight)`
  - Changes the weight of a given face.
  - **Parameters:**
    - `face` (str or number): The face value to change.
    - `weight` (float): The new weight.
  - **Raises:**
    - `IndexError` if the face is not found.
    - `TypeError` if the weight is not numeric.
  - **Returns:** None.

- `roll(num_rolls: int = 1)`
  - Rolls the die a specified number of times.
  - **Parameters:**
    - `num_rolls` (int, default=1): Number of rolls.
  - **Returns:** List of outcomes.

- `show()`
  - Displays the current faces and weights.
  - **Parameters:** None.
  - **Returns:** `pandas.DataFrame` with faces and their corresponding weights.

---

### Game Class

Manages the playing of a game with one or more dice.

**Attributes:**
- None publicly accessible.

**Methods:**
- `__init__(dice: list)`
  - Initializes the game with a list of Die objects.
  - **Parameters:**
    - `dice` (list): A list containing Die objects.
  - **Returns:** None.

- `play(num_rolls: int)`
  - Rolls all dice for a given number of times.
  - **Parameters:**
    - `num_rolls` (int): Number of times to roll the dice.
  - **Returns:** None.

- `show(form: str = 'wide')`
  - Displays the results of the most recent play.
  - **Parameters:**
    - `form` (str, default='wide'): Format of results. Can be `'wide'` or `'narrow'`.
  - **Raises:**
    - `ValueError` if form is not `'wide'` or `'narrow'`.
  - **Returns:** `pandas.DataFrame` of results.

---

### Analyzer Class

Analyzes the results from a completed game.

**Attributes:**
- None publicly accessible.

**Methods:**
- `__init__(game: Game)`
  - Initializes the analyzer with a Game object.
  - **Parameters:**
    - `game` (Game): A completed Game object.
  - **Raises:**
    - `ValueError` if input is not a Game object.
  - **Returns:** None.

- `jackpot()`
  - Counts the number of rolls where all faces match.
  - **Parameters:** None.
  - **Returns:** Integer count of jackpots.

- `face_counts_per_roll()`
  - Counts the number of times each face appears in each roll.
  - **Parameters:** None.
  - **Returns:** `pandas.DataFrame` where rows are rolls and columns are faces.

- `combo()`
  - Counts distinct combinations (order-independent) of rolled faces.
  - **Parameters:** None.
  - **Returns:** `pandas.DataFrame` with MultiIndex of combinations and counts.

- `permutation()`
  - Counts distinct permutations (order-dependent) of rolled faces.
  - **Parameters:** None.
  - **Returns:** `pandas.DataFrame` with MultiIndex of permutations and counts.

---

# Notes

- All classes and methods include docstrings for easy reference.
- All inputs are validated, and meaningful errors are raised where appropriate.
