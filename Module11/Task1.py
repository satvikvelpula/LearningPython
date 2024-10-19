class Publication:
    def __init__(self, publication_name):
        self.publication_name = publication_name

    def print_information(self):
        pass

class Book(Publication):
    def __init__(self, publication_name, author, page_count):
        super().__init__(publication_name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.publication_name} | Author: {self.author} | Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, publication_name, chief_editor):
        super().__init__(publication_name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.publication_name} | Chief Editor: {self.chief_editor}")

# Main program

publication1 = Magazine("Donald Duck", "Aki Hyyppä")
publication2 = Book("Compartment No. 6", "Rosa Liksom", 192)

publication1.print_information()
publication2.print_information()

