sentence = input().split()
word_s_end = []

for n in range(len(sentence)):
    if sentence[n].endswith('s'):
        word_s_end.append(sentence[n])

print('_'.join(word_s_end))
