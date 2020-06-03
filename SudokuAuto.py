input = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(ip):
    find = find_empty(ip)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(ip, i, (row, col)):
            ip[row][col] = i

            if solve(ip):
                return True

            ip[row][col] = 0

    return False

def valid(ip, num, pos):

    # Check row
    for i in range(len(ip[0])):
        if ip[pos[0]][i] == num and pos[1] != i:
            return False

    # Check col
    for i in range(len(ip[0])):
        if ip[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if ip[i][j] == num and (i, j) != pos:
                return False

    return True


def print_input(ip):

    for i in range(len(ip)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(ip)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(ip[i][j])
            else:
                print(str(ip[i][j]) + " ", end="")


def find_empty(ip):
    for i in range(len(ip)):
        for j in range(len(ip[0])):
            if ip[i][j] == 0:
                return (i, j)
    return None

print_input(input)
solve(input)
print("___________________")
print_input(input)