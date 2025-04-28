import pandas as pd

class Game:
    """
    A game consists of rolling one or multiple dice of the same kind multiple times
    
    Attributes:
        _dice (list): List of Die objects
        _play_results (DataFrame): Private dataframe storing the results of the most recent play
    """
    
    def __init__(self, dice):
        """
        Initialize the Game with a list of dice

        Args:
            dice (list): A list containing one or more Die objects
        """
        self._dice = dice
        self._play_results = None

    def play(self, num_rolls):
        """
        Play the game by rolling all dice a given number of times

        Args:
            num_rolls (int): Number of times to roll the dice
        Saves:
            _play_results (DataFrame): Roll results with wide format
        """
        results = {}

        for i, die in enumerate(self._dice):
            results[i] = die.roll(num_rolls)

        self._play_results = pd.DataFrame(results)
        self._play_results.index.name = 'roll_number'

    def show(self, form='wide'):
        """
        Show the results of the most recent play

        Args:
            form (str): Format of the result ('wide' or 'narrow'). Defaults to 'wide'
        Returns:
            pandas.DataFrame: Copy of the play results in the requested format
        Raises:
            ValueError: If form is not 'wide' or 'narrow'
        """
        if self._play_results is None:
            raise ValueError("No results to show; play the game first")

        if form == 'wide':
            return self._play_results.copy()
        elif form == 'narrow':
            return self._play_results.stack().to_frame('face')
        else:
            raise ValueError("Invalid form argument. Choose 'wide' or 'narrow'")