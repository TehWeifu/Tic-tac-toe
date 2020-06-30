n_floors = int(input())

n_stars = 2 * n_floors - 1
n_spaces = 0

floors = []

for n in range(n_floors):
    floors.append(' ' * (n_spaces // 2) + '#' * n_stars + ' ' * (n_spaces // 2))
    n_stars -= 2
    n_spaces += 2

floors = reversed(floors)
print('\n'.join(floors))
