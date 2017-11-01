class User:
    pass # 中身のないクラスを意味する。

tom = User() # インスタンス
tom.name = "tom"
tom.score = 20

bob = User()
bob.name = "bob"
bob.level = 5

print(tom.name)
print(bob.level)
