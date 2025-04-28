import numpy as np
import pandas as pd

class Die:
    """
    A die has N sides or faces
    Faces can be strings or numbers
    Weights default to 1.0 but can be changed after initialization
    
    Attributes:
        _die (DataFrame): Private dataframe with faces and weights
    """
    
    def __init__(self, faces):
        """
        Initialize a die with faces and default weights of 1.0

        Args:
            faces (numpy.ndarray): Array of distinct face values (numeric/strings)
        
        Raises:
            TypeError: If faces is not a numpy array
            ValueError: If faces are not distinct
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array!")
        
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Faces must be distinct!")
        
        self._die = pd.DataFrame({
            'face': faces,
            'weight': np.ones(len(faces))
        }).set_index('face')

    def change_weight(self, face, weight):
        """
        Change the weight of a single face.

        Args:
            face (str/number): Face value to change
            weight (float/integer): New weight (must be numeric and not negative)
        
        Raises:
            IndexError: When face is not found
            TypeError: When weight is not numeric (integer/float)
        """
        if face not in self._die.index:
            raise IndexError("Face not found in die!")
        
        try:
            weight = float(weight)
        except ValueError:
            raise TypeError("Weight must be numeric or castable to float!")
        
        self._die.at[face, 'weight'] = weight

    def roll(self, num_rolls=1):
        """
        Roll the die a given number of times.

        Args:
            num_rolls (int): Number of rolls (default 1)
        
        Returns:
            list: Outcomes of rolls
        """
        outcomes = self._die.sample(
            n=num_rolls, 
            weights=self._die['weight'], 
            replace=True
        ).index.tolist()
        return outcomes

    def show(self):
        """
        Show the die's current faces and weights

        Returns:
            pandas.DataFrame: Copy of die's faces and weights
        """
        return self._die.copy()