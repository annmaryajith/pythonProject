class Publisher:
    def __init__(self, name):
        self.name = name
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
class Python(Book):
    def __init__(self, name, title, author, price, noofpages):
        super().__init__(name, title, author)
        self.price = price
        self.noofpages = noofpages
    def show(self):
          print("Publisher: ", self.name)
          print("Book name: ", self.title)
          print("Author name: ", self.author)
          print("Price: ", self.price)
          print("Number of pages: ", self.noofpages)
details=Python("Rupa & Co.", "One Indian Girl", "Chetan Bhagat",126,
280)
details.show()