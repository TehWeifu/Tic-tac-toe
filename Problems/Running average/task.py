digits_string = input()
digit_array = []
average_array = []

for n in range(len(digits_string)):
    digit_array.append(int(digits_string[n]))

for n in range(len(digit_array) - 1):
    average_array.append((digit_array[n] + digit_array[n+1]) / 2)

print(average_array)
