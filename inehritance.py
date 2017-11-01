# クラスの継承
# 既存のクラスをもとに新しいクラスを作る。
# User（親クラス、スーパークラス） -> AdminUser（子クラス、サブクラス）

class User:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hi {0}".format(self.name))

class AdminUser(User): # Userクラスを継承
    def __init__(self, name, age):
        super().__init__(name) # 親クラスのコンストラクタを実行
        self.age = age

    def say_hello(self):
        print("hello {0} ({1})".format(self.name, self.age))

    # オーバーライド（override）
    def say_hi(self):
        print("[admin] hi {0}".format(self.name))

bob = AdminUser("bob", 23)
print(bob.name)
bob.say_hello()
bob.say_hi()
