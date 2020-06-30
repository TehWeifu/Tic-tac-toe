sentence = input()
sentence = sentence.lower()
sentence = sentence.split('_')

for n in range(len(sentence)):
    sentence[n] = sentence[n].capitalize()

print(''.join(sentence))
