wrongspot = {}
correctspot = {}
correctspot2 = {}
wrongspot2 = {}

with open("words.txt", "r") as f:
  contents = f.readlines()

words = []
for word in contents:
  words.append(word[:-1])

words.remove('pupa')
words.append('pupal')


print("Suggested guesses: oater, crane")

gameOver = False
print(len(words))

while gameOver == False:
  x = int(input("1: gray, 2: yellow, 3: green, 4: continue \n"))

  if x == 1:
    letter = input("What letter is it?")
    for x in range(0, 5):
        for word in words:
            if letter in word:
                if (letter in correctspot2):
                    for z in correctspot2[letter]:
                        if word[z-1] == letter:
                            pass
                        else:
                            words.remove(word)
                else:
                    words.remove(word)
    
  elif x == 2:
    letter = input("What letter was it?")
    spot = int(input("What spot is it in? 1 for first letter, 5 for last"))
    if letter in wrongspot:
      wrongspot[letter].append(spot)
    else:
      wrongspot[letter] = [spot]
    length = len(words)
    i = 0
    new_list = []
    while i < length:
        word = words[i]
        for letter in wrongspot:
            spot = wrongspot[letter]
            for z in spot:
                print(word[z-1])
                print(letter)
                if (not word[z-1] == letter) and (not (word in new_list)) and (letter in word):
                    new_list.append(word)
        i+=1
    words = new_list
    if len(wrongspot) != 0:
        wrongspot2.update(wrongspot)
        wrongspot.clear()

  elif x == 3:
    letter = input("What letter was it")
    spot = int(input("What spot is it in? 1 for first letter, 5 for last"))
    if letter in correctspot:
      print("I already know!")
    else:
      correctspot[letter] = [spot]
    length = len(words)
    i = 0
    new_list = []
    while i < length:
        word = words[i]
        for letter in correctspot:
            spot = correctspot[letter]
            for z in spot:
                print(z)
                print(word[z-1])
                print(letter)
                if (word[z-1] == letter) and (not (word in new_list)):
                    new_list.append(word)
        i+=1
    words = new_list
    if len(correctspot) != 0:
        correctspot2.update(correctspot)
        correctspot.clear()

  else:
    pass

  print(words)
  print(len(words))


