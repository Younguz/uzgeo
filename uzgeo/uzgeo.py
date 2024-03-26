"""Main module."""

import ipyleaflet

class Map(ipyleaflet.Map):
    """
    Calculate the average value of a sequence.  

    Args:
    sequence (list or tuple): The sequence of numbers.

    Returns:
    float: The average value of the sequence.
    """
    def __init__(self, center=[20,0], zoom=2, **kwargs):
        """
        Calculate the average value of a sequence.  

        Args:
        sequence (list or tuple): The sequence of numbers.

        Returns:
        float: The average value of the sequence.
        """
        super().__init__(center=center, zoom=zoom, **kwargs) 
        self.add_control(ipyleaflet.LayersControl())
