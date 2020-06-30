# put your python code here
grades = input().split()
a_count = 0

for n in range(len(grades)):
    if grades[n] == 'A':
        a_count += 1

print(round(a_count / len(grades), 2))
