# if
score = int(input("score ? "))
# ユーザーからの入力を受け付ける。また入力を受け付ける際に、"score ? "と聞く。その入力をint型にキャストする。

# 比較演算子 > >= < <= == !=
if score > 80: # 必ず字下げを行う。
    print("Great!")
elif score > 60:
    print("Good!")
else:
    print("so so ...")

print("Great!" if score > 80 else "so so ...")