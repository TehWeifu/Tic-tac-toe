number_string = input()
new_list = [int(x) for x in number_string if int(x) % 2 == 1]
print(new_list)
