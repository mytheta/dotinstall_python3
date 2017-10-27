name = "taguchi"
score = 52.8

print("name: %s, score: %f" % (name, score)) # 整数の場合は、%d
print("name: %-10s, score: %10.2f" % (name, score)) # -をつけたら左ぞろえ、デフォルトは右ぞろえ

print("name: {0}, score: {1}".format(name, score))
print("name: {0:>10s}, score: {1:<10.2f}".format(name, score)) # >は右ぞろえ、<は左ぞろえ
