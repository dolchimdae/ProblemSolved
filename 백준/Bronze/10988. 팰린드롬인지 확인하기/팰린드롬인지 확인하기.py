word = input().rstrip()
new_word = list(word)
new_word.reverse()
new_word = ''.join(new_word)
if word == new_word:
  print(1)
else:
  print(0)