class farmer:
    def __init__(self):
        self.color="black"

    def skills(self):
        self.driving="car"
        print("Heavy Driver")
    def occupation(self):
        print("he is a farmer")
class son(farmer):
    def __init__(self):
        super().__init__()

    def myskills(self):
        print("I also drive car")
    def occupation(self):
        super().occupation()
        print("he is ingenier")

nemo=son()
nemo.occupation()