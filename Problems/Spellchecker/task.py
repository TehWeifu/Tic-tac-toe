dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input().split()
misspelled = []

for n in range(len(sentence)):
    if sentence[n] not in dictionary:
        misspelled.append(sentence[n])

if len(misspelled) > 0:
    print('\n'.join(misspelled))
else:
    print("OK")
