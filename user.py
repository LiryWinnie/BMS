# User类
class User(object):
    #构造函数
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    #登录校验函数
    def login(self):
        #打开文件 r:阅读
        with open("./files/users.txt","r") as f:
            for line in f.readlines():
                uname, upass = line.strip().split(",") #strip():去掉/n  split 拆分string
                if self.username == uname and self.password == upass:
                    return True
            else:
                return False
    
    def register(self):
        #打开文件 a:追加写入
        with open("./files/users.txt","a") as f:
            f.write(self.username+","+self.password+"\n")