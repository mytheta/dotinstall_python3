# 関数

# def say_hi():
#     print("hi")
#
#  say_hi()

def say_hi(name, age = 20): # ageに引数が渡されなければ、20で初期化される。
    print("hi {0} ({1})".format(name, age))

def str_hi(): # 返り値を持つ関数
    return "hi"
    print("hello") # 実行されない。

def hi_pass(): # 関数名だけ定義して、処理は後で考えるとき等に使う。
    pass # "None"が返ってくる。

say_hi("tom", 23) # tom (23)
say_hi("bob", 21) # bob (21)
say_hi("steve") # steve (20)
say_hi(age = 18, name = "rick") # 引数の名前を直接指定する。

msg = str_hi()
print(msg)

msg = hi_pass()
print(msg)

