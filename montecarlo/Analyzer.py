import pandas as pd
from collections import Counter

class Analyzer:
    """
    An Analyzer object takes the results of a single Game object and computes various descriptive statistical properties about it

    Attributes:
        _game (Game): Game object
        _jackpot_count (int): Number of jackpots
        _face_counts_per_roll (DataFrame): Face counts per roll
        _combo_counts (DataFrame): Distinct combinations and their counts
        _perm_counts (DataFrame): Distinct permutations and their counts
    """

    def __init__(self, game):
        """
        Initialize the Analyzer with a Game object.

        Args:
            game (Game): An instance of the Game class
        Raises:
            ValueError: If input is not a Game object
        """
        if not isinstance(game, Game):
            raise ValueError("Analyzer must be initialized with a Game object")

        self._game = game
        self._jackpot_count = None
        self._face_counts_per_roll = None
        self._combo_counts = None
        self._perm_counts = None

    def jackpot(self):
        """
        Compute the number of jackpots (all faces in a roll are identical)
        Returns:
            int: Number of jackpots
        """
        df = self._game.show('wide')
        self._jackpot_count = (df.nunique(axis=1) == 1).sum()
        return self._jackpot_count

    def face_counts_per_roll(self):
        """
        Compute how many times each face appeared in each roll

        Returns:
            pandas.DataFrame: Rows are roll numbers, columns are faces, cells are counts
        """
        df = self._game.show('wide')
        faces = pd.unique(df.values.ravel())
        counts = []

        for _, row in df.iterrows():
            row_count = Counter(row)
            counts.append([row_count.get(face, 0) for face in faces])

        self._face_counts_per_roll = pd.DataFrame(
            counts,
            columns=faces,
            index=df.index
        )
        return self._face_counts_per_roll

    def combo(self):
        """
        Compute distinct combinations of faces rolled (order-independent) and their counts

        Returns:
            pandas.DataFrame: MultiIndex of combinations, column for counts
        """
        df = self._game.show('wide')
        combos = df.apply(lambda x: tuple(sorted(x)), axis=1)

        self._combo_counts = combos.value_counts().to_frame('count')
        self._combo_counts.index.names = [f'die_{i}' for i in range(df.shape[1])]
        return self._combo_counts

    def permutation(self):
        """
        Compute distinct permutations of faces rolled (order-dependent) and their counts

        Returns:
            pandas.DataFrame: MultiIndex of permutations, column for counts
        """
        df = self._game.show('wide')
        perms = df.apply(lambda x: tuple(x), axis=1)

        self._perm_counts = perms.value_counts().to_frame('count')
        self._perm_counts.index.names = [f'die_{i}' for i in range(df.shape[1])]
        return self._perm_counts