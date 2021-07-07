# This is some practice on classes, inheritance, and child classes customizing
# the behavior of parent classes with .super().

class Trail():
    """A class to represent trails"""
    def __init__(self, dest, len=0):
        self.dest = dest
        self.len = len
    def describe_trail(self):
        """Print a description of trail"""
        desc = f'This trail goes to {self.dest}.'
        if self.len:
            desc += f'\nThis trail is {self.len}km long.'
        print(desc)
    def run_trail(self):
        """Simulates running the trail"""
        print(f'Running to {self.dest}.')

class BikeTrail(Trail):
    """Represent a bike trail. Child class of Trail"""
    def __init__(self, dest, len=0):
        super().__init__(dest, len)
        self.paved = True
        self.bikes_only = True
    def ride_trail(self):
        """Simulate riding the trail"""
        print(f'Riding to {self.dest}.')
    def run_trail(self):
        """Simulate running the trail"""
        if self.bikes_only:
            print("You can't run this trail--it's bikes only!")
        else:
            super().run_trail()

"""
Sample function calls from these parent, child classes:

verst = Trail('Mt Verstovia', 4)
    verst.describe_trail():
        # This trail goes to Mt Verstovia.
        # This trail is 4km long.
    verst.run_trail():
        # Running to Mt. Verstovia.
ms = Trail('Middle Sister')
    ms.describe_trail():
        # This trail goes to Middle Sister.
        # (No line here because default len = 0)
hm = BikeTrail('Harbor Mountain', 13)
    hm.ride_trail():
        # Riding to Harbor Mountain.
    hm.run_trail():
        # You can't run this trail--it's bikes only!


To run in another program:
import trails OR
from trails import Trail/BikeTrail

ms = trails.Trail('Middle Sister', 5)
    ms.describe_trail()
        # This trail goes to Middle Sister. This trail is 5km long.

hm = trails.BikeTrail('Harbor Mountain')
    # and so on...
"""