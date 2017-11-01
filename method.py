class User:
    count = 0
    # コンストラクタ（メソッドの一種）
    def __init__(self, name):
        User.count += 1
        self.name = name

    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))

    # クラスメソッド（デコレーター）
    @classmethod
    def show_info(cls): # このクラス自身を意味する"cls"
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

tom.say_hi()
bob.say_hi()

User.show_info()
