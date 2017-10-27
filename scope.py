# 関数内の変数

msg = "hello" # グローバル変数

def say_hi1():
    msg = "hi" # ローカル変数。この関数内でのみ有効
    print(msg)

def say_hi2():
    print(msg)

def say_hi3():
    global msg # グローバル変数を使う宣言。
    msg = "hello global" # グローバル変数

say_hi1() # hi
print(msg) # hello

say_hi2() # hello

say_hi3()
print(msg) # hello global
