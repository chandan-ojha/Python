class Phone:
    def __init__(self):
        print("I am in phone class")

class Samsung(Phone):
    def __init__(self):
        super().__init__()
        print("I am in Samsung class")
s=Samsung()

