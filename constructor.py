class User:
    # クラス変数
    count = 0
    def __init__(self, name): # コンストラクタ
        User.count += 1
        # インスタンス変数
        self.name = name

print(User.count) # 0
tom = User("tom")
print(User.count) # 1
bob = User("bob")
print(User.count) # 2

print(tom.name)
print(bob.name)

print(tom.count) # 2 （インスタンス変数がなければ、クラス変数が呼び出される。）
