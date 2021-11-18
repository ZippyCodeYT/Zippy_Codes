










text = "I love Python"
for i in range(30):
  print(text)

for k in range(3):
  for i in range(6):
    print(" " * i, text)
  for i in range(6):
    print(" " * (5-i), text)

for k in range(3):
  for i in range(len(text)):
    print(text[i:], text[:i])

for k in range(3):
  for i in range(6):
    print(text[:6], i * " ",
          text[6:])
  for i in range(6):
    print(text[:6], (5 - i) * " ",
          text[6:])

trim = "IlovePython"
for n in range(5):
  for i in range(5):
    print(trim[:5]+ i*" "+
      trim[5]+ (5-i)*" " + trim[6:])
  for i in range(5):
    print(trim[:5]+ (5-i)*" "+
          trim[5]+ i*" " + trim[6:])


for i in range(len(trim)):
  for j in range(5):
    print(trim[:i], (4-j)*" ",
          trim[i],j*" ", trim[i+1:])

for i in range(20):
  print(trim)









