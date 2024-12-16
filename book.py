class Book(object):
    def __init__(self, bookname, author=None, num=None, addr=None):
        self.name = bookname
        self.author = author
        self.num = num
        self.addr = addr
        self.file_path = "./files/books.txt"
        self.booklist = self.getbook()
    
    def getStr(self):
        return self.name+","+self.author+","+self.num+","+self.addr+"\n"
    
    def addBook(self):
        if self.isExistBook(self.name):
            return False
        else:
            self.booklist.append(self)
            return True
        
    def isExistBook(self,name):
        for book in self.booklist:
            if book.name == name:
                # 因为后面需要
                return book
        else:
            return
    
    def refresh(self):
        with open(self.file_path,"w") as f:
            for b in self.booklist:
                f.write(b.getStr())
    
    def getbook(self):
        blist = []
        with open(self.file_path,"r") as f:
            for line in f.readline():
                list1 = line.strip().split(",")
                if len(list1)<4:
                    continue
                else:
                    blist(Book(list1[0],list1[1],list1[2],list1[3]))
        return blist

        