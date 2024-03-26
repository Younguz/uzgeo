"""Main module."""

import ipyleaflet

class Map(ipyleaflet.Map):
    """
    This is the map class that inherits from ipyleaflet.Map.

    Args:
        ipyleaflet.Map (Map): The ipyleaflet.Map class.
    """
    def __init__(self, center=[20,0], zoom=2, **kwargs):
        """
        Initialize the map.

        Args:
            center (list): Set the center of the map. Defaults to [20, 0].
            zoom (int): Set the zoom level of the map. Defaults to 2.

        """
        super().__init__(center=center, zoom=zoom, **kwargs) 
        self.add_control(ipyleaflet.LayersControl())
