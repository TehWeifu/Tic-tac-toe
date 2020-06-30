text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
new_list = []
number = int(input())
for group in text:
    for word in group:
        if len(word) <= number:
            new_list.append(word)

print(new_list)
