import ipdb

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        contract_list = []
        for contract_obj in Contract.all:
            if contract_obj.author is self:
                contract_list.append(contract_obj)
        return contract_list
    
    def books(self):
        book_list = []
        for book_obj in Contract.all:
            if book_obj.author is self:
                book_list.append(book_obj.book)
        return book_list
    
    def sign_contract(self, book, date, royalties):
        # ipdb.set_trace()
        if isinstance(book, Book):
            contract = Contract(self, book, date, royalties)
            return contract
        else:
            print('invalid contract')

    def total_royalties(self):
        # ipdb.set_trace()
        total = 0
        for contract in self.contracts():
            royalty = contract.royalties
            total += royalty
        return total
    
    def __repr__(self):
        return f'<Author {self.name} >'    

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        contract_list = []
        for contract_obj in Contract.all:
            if contract_obj.book is self:
                contract_list.append(contract_obj)
        return contract_list
    
    def authors(self):
        author_list = []
        for contract_obj in Contract.all:
            if contract_obj.book is self:
                author_list.append(contract_obj.author)
        return author_list


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # if not isinstance(author, Author):
        #     raise Exception("invalid Author")
        # else:
        #     self.author = author
        # if not isinstance(book, Book):
        #     raise Exception("inavlid Book")
        # else:
        #     self.book = book
        # if not isinstance(date, str):
        #     raise Exception("invalid date")
        # else:
        #     self.date = date
        # if not isinstance(royalties, int):
        #     raise Exception("invalid royalties")
        # else:
        #     self.royalties = royalties
        # self.all.append(self)

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


author = Author("Name")
book = Book("Title")

book2 = Book("Title 2")
book3 = Book("Title 3")

Contract(author, book, "01/01/2001", 10)
Contract(author, book2, "01/01/2001", 20)
Contract(author, book3, "01/01/2001", 30)
    
contract = author.sign_contract(book, "01/01/2001", 60000)

author2 = author.total_royalties()