grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

newString = ''

for i in range(len(grid)):
    newString += str(grid[i][0])

newString1 = '\n'
for i in range(len(grid)):
    newString1 += str(grid[i][1])

newString2 = '\n'
for i in range(len(grid)):
    newString2 += str(grid[i][2])

newString3 = '\n'
for i in range(len(grid)):
    newString3 += str(grid[i][3])

newString4 = '\n'
for i in range(len(grid)):
    newString4 += str(grid[i][4])

newString5 = '\n'
for i in range(len(grid)):
    newString5 += str(grid[i][5])

print(newString+newString1+newString2+newString3+newString4+newString5)
