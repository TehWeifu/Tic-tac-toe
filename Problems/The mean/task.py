numbers_string = input()
new_list = [int(x) for x in numbers_string]

print(sum(new_list) / len(new_list))
