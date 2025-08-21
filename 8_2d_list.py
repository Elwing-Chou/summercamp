board = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19],
]
print(board[1][2])
print(board[2][1])
board[2][1] = 88
print(board)

total = [i+1 for i in range(20)]
print(total)

total = [0] * 20
print(total)

total = [[0] * 3 for i in range(4)]
print(total)