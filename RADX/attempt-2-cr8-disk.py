#objective disk?
class Disk(object):
    """
    Simulate a particle falling due to Earth's gravity. Particle is stationary at first

    Args:
        height (float): a height in meters
        dt (float): timestep of the simulation in seconds
    """
    def __init__(self, raduis):
        """
        Function that is run to initialize the class.

        The input `self` is required for functions that belong to an object,
        meaning that you want to make the function access and/or depend on the 
        attributes of the object (e.g., self.time, and self.velocity below)
        """
        # let's initalize it's parent class (empty for now because it is a blank class)
        super().__init__()

        # note that we are not using the astropy.units class here as we haven't talked about it yet! But it could be useful!
        self.innerbound = 0 # center coord [tbd]
        self.outerbound = raduis # outer coord[tbd]
