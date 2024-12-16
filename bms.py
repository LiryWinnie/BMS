from win.bmswin import Ui_MainWindow
from user import User
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from book import Book
class BMSManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(BMSManager,self).__init__()
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.click_add)
        self.pushButton_7.clicked.connect(self.click_del)
        self.pushButton_8.clicked.connect(self.click_search)
        self.pushButton_9.clicked.connect(self.click_modify)
        self.pushButton_4.clicked.connect(self.add_book)
        self.pushButton_2.clicked.connect(self.del_book)
    def click_add(self):
        """ 
            跳转添加图书页面
        """
        self.stackedWidget.setCurrentIndex(0)
 
    def click_del(self):
        """ 
            跳转删除图书页面
        """
        self.stackedWidget.setCurrentIndex(1)

    def click_search(self):
        """ 
            跳转查找图书页面
        """
        self.stackedWidget.setCurrentIndex(2)
 
    def click_modify(self):
        """ 
            跳转修改信息页面
        """
        self.stackedWidget.setCurrentIndex(3)
    
    def add_book(self):
        """ 
            添加图书操作
        """
        bookname = self.lineEdit_2.text()
        author = self.lineEdit_6.text()
        num = self.lineEdit_7.text()
        address = self.lineEdit_8.text()

        new_book = Book(bookname,author,num,address)
        if new_book.addBook():
            new_book.refresh()
            QMessageBox.information(None,"信息","添加成功！",QMessageBox.Close)
        else:
            QMessageBox.warning(None,"错误","书名已存在！",QMessageBox.Close)
    
    def del_book(self):
        bookname = self.lineEdit.text()
        new_book = Book(bookname)
        book = new_book.isExistBook(bookname)
        if book:
            book.booklist.remove(book)
            book.refresh()
        else:
            QMessageBox.warning(None,"错误","书名不存在！",QMessageBox.Close)

