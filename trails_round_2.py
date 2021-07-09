# trails2: the second practice runthrough

class Trail():
    def __init__(self, dest, len=0):
        self.dest = dest        # By passing both arguments to 'self', it's easier to inherit them
        self.len = len          # as just one argument in other functions e.g. describe_trail(self).
    def run_trail(self):
        print(f"I'm running to {self.dest}.")
    def describe_trail(self):
        desc = f'This trail leads to {self.dest}.'
        if self.len:            # If there's a value given for len, print this. If not, then do nothing.
            desc += f'\nThis trail is {self.len}km long.\n'
        print(desc)

class BikeTrail(Trail):         # Child class. Inherits from parent class Trail()
    def __init__(self, dest, len=0):
        super().__init__(dest, len=0)       # super(). overwrites behavior of the inherited function.
        self.paved = True
        self.bikes_only = True
    def ride_trail(self):
        print(f"I'm riding my bike to {self.dest}.")
    def run_trail(self):
        if self.bikes_only:
            print("You can't run this trail - it's just for bikes.")
        else:
            super().run_trail()

verst = Trail("Mt. Verstuvius", 6)
verst.run_trail()
verst.describe_trail()

hm = BikeTrail('Harbor Mountain', 13)
hm.describe_trail()
hm.ride_trail()
hm.run_trail()