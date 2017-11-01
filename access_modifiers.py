class User:
    def __init__(self, name):
        # self._name = name _を前につけると「外からアクセスしないでね。」という意味になる。
        self.__name = name # __を前につけると「外からアクセスできなくなる。」

    def say_hi(self):
        print("hi {0}".format(self.name))

tom = User("tom")
# print(tom._name) アクセスできちゃう。
# print(tom.__name) アクセスできない。
print(tom._User__name) # アクセスできちゃう…。

