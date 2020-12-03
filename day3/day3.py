

def tree_counter(horizontal, vertical):
    lines = []
    with open('input') as f:
        for line in f.readlines():
            lines.append(line.strip())

    trees, x, y = 0, 0, 0

    while y < len(lines):
        if lines[y][x % len(lines[0])] == '#':
            trees += 1
        x += horizontal
        y += vertical

    return trees

total = 1
slopes = [tree_counter(1, 1), tree_counter(3, 1), tree_counter(5, 1), tree_counter(7, 1), tree_counter(1, 2)]
for slope in slopes:
    total = total * slope

print(tree_counter(3, 1))
print(total)
