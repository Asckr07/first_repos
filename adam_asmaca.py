import random
liste = ["python","print","random","while","choice"]
kelime = random.choice(liste)
adam = ['''
  +----+
  o    |
 /|\   |
 / \   |
      ---''','''
 +----+
  o    |
 /|\   |
 /     |
      ---''','''
 +----+
  o    |
 /|\   |
       |
      ---''','''
 +----+
  o    |
 /|    |
       |
      ---''','''
 +----+
  o    |
 /     |
       |
      ---''','''
 +----+
  o    |
       |
       |
      ---''','''
 +----+
       |
       |
       |
      ---''']

dogruHarf = []
yanlisHarf = []
hak = len(adam)

while hak > 0:
    out = ""
    for h in kelime:
        if h in dogruHarf:
            out+= h
    else:
        out+= "_"
    if out == kelime:
        break
    print("Kelime: ",out)
    print(adam[hak-1])
    girHarf = input()
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print(girHarf, "Zaten girildi")
    elif girHarf in kelime:
        print("Doğru harf")
        dogruHarf.append(girHarf)
    else:
        print("Yanlış harf..!")
        hak-=1
        yanlisHarf.append(girHarf)

if hak != 0:
    print("Tebrikler.. Kazandınız.. Kelimeniz : ",kelime)
else:
    print("Maalesef... Kaybettin.. Kelime : ",kelime, "idi")
