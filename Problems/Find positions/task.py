# put your python code here
sequence = input().split()
number = input()
appearances = []

for n in range(len(sequence)):
    if sequence[n] == number:
        appearances.append(str(n))

if len(appearances) > 0:
    print(' '.join(appearances))
else:
    print("not found")
