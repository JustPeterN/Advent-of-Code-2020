def part1():
    file1 = open('input', 'r')
    lines = file1.readlines()

    for x in lines:
        for y in lines:
            if int(y) + int(x) == 2020:
                print(int(y) * int(x))

def part2():
    file1 = open('input', 'r')
    lines = file1.readlines()

    for x in lines:
        for y in lines:
            for z in lines:
                if int(y) + int(x) + int(z) == 2020:
                    print(int(y) * int(x) * int(z))
