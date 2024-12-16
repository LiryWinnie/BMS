from win.mywin import Ui_MainWindow
from bms import BMSManager
from user import User
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import sys
from PyQt5 import QtCore
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class LoginManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginManager,self).__init__()
        # 展示界面
        self.setupUi(self)
        # 四个按钮设置等待槽函数
        self.pushButton.clicked.connect(self.click_register)
        self.pushButton_2.clicked.connect(self.click_login)
        self.pushButton_3.clicked.connect(self.user_login)
        self.pushButton_4.clicked.connect(self.user_register)

    @QtCore.pyqtSlot()
    def click_register(self):
        """ 
            跳转注册页面
        """
        self.stackedWidget.setCurrentIndex(1)
    
    @QtCore.pyqtSlot()
    def click_login(self):
        """ 
            跳转登录页面
        """
        self.stackedWidget.setCurrentIndex(0)
    
    @QtCore.pyqtSlot()
    def user_login(self):
        # 获取到两个输入框的值
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if (username is None) or (password is None):
            QMessageBox.warning(None,"错误","用户名或密码为空",QMessageBox.Close)
        else:
            now_user = User(username,password)
            if(now_user.login()):
                #跳转到第二页面（图书管理页面）
                self.hide() #当前页面隐藏
                self.bms_win = BMSManager() #新建第二个页面的对象
                self.bms_win.show() #展示第二个页面
            else:
                QMessageBox.warning(None,"错误","用户名或密码错误",QMessageBox.Close)
    
    @QtCore.pyqtSlot()
    def user_register(self):
        username = self.lineEdit_3.text()
        password1 = self.lineEdit_4.text()
        password2 = self.lineEdit_5.text()
        if (username is None) or (password1 is None) or (password2 is None):
            QMessageBox.warning(None,"错误","用户名或密码为空",QMessageBox.Close)
        elif password2!=password1:
            QMessageBox.warning(None,"错误","两次输入的密码不一致！请重新输入",QMessageBox.Close)
        else:
            now_user = User(username,password1)#创建用户对象
            now_user.register()
            QMessageBox.information(None,"提示","注册成功，请登录！",QMessageBox.Close)
            # 注册成功跳转到登录页面
            self.click_login()

class BMSManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(BMSManager,self).__init__()
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.click_add)
        self.pushButton_7.clicked.connect(self.click_del)
        self.pushButton_8.clicked.connect(self.click_search)
        self.pushButton_9.clicked.connect(self.click_modify)
        self.pushButton_4.clicked.connect(self.add_book)
    
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
            QMessageBox.information(None,"信息","添加成功！",QMessageBox.Close)
        else:
            QMessageBox.warning(None,"错误","书名已存在！",QMessageBox.Close)
    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginManager()
    ex.show()
    sys.exit(app.exec_())
