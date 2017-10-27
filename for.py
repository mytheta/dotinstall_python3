# for

# for 変数 in データの集合:
#   処理
# データの集合を一つずつ指示した変数に格納して処理を行う。

for i in range(0, 10): # 0から10を含まない(0から9)数値データの集合
    print(i)

for i in range(10): # 0は省略できる。
    print(i)
else:
    print("end") # forを抜けた際の処理

for i in range(0, 10):
    if i == 5:
        # break
        continue # 次のループにうつる。
    print(i)
