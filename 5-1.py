class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def get_info(self):
        return "Название книги: {}, Автор: {}, Год издания: {}".format(self.title, self.author, self.year)


harry = Book("Гарри Поттер", "Джоан Роулинг", "1997")
print(harry.get_info())