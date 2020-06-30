sequence = input()
new_list = []
sequence_sum = 0

for x in sequence:
    sequence_sum += int(x)
    new_list.append(sequence_sum)

print(new_list)
