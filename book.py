class Book(object):
    def __init__(self, bookname, author, num, addr):
        self.bookname = bookname
        self.author = author
        self.num = num
        self.addr = addr
        self.file_path = "./file/books"
        self.booklist = self.getbook()
    
    def addBook(self,book):
        if self.isExistBook(book.name):
            return False
        else:
            self.booklist.append(book)
            return True
        
    def isExistBook(self,name):
        for book in self.booklist:
            if book.name == name:
                # 因为后面需要
                return book
        else:
            return
    
    def getbook(self):
        blist = []
        with open(self.file_path,"r") as f:
            for line in f.readline():
                bn, au, nu, ad = line.strip().split(",")
                blist(Book(bn,au,nu,ad))

        