class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")


class Samsung(Phone):
    def photo(self):
        print("you can take photo")


s=Samsung()
s.message()
s.call()
s.photo()
print(issubclass(Samsung,Phone))