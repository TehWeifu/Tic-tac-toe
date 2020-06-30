sentence = input().split()


for n in range(1, len(sentence)):
    sentence[n] = sentence[n].capitalize()

print(''.join(sentence))
