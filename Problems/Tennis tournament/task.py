number_lines = int(input())
winners_list = []

for n in range(number_lines):
    name_string = input()
    name_list = name_string.split()
    if name_list[1] == "win":
        winners_list.append(name_list[0])

print(winners_list)
print(len(winners_list))
