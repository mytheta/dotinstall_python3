# while

i = 0
while i < 10: # 字下げを忘れない。
   print(i)
   i += 1
else: # whileからぬけたときの処理
   print("end")

i = 0
while i < 10:
   if i == 5:
      break # 途中で抜けるとelseの処理が行われない。
   print(i)
   i += 1
else:
   print("end")
