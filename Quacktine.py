def calculate_wall(table):
    wall = 0
    rows = len(table)
    cols = len(table[0])

    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 0:
                if i > 0 and table[i - 1][j] == 1: # Up
                    wall += 1
                if i < rows - 1 and table[i + 1][j] == 1: # Down
                    wall += 1
                if j > 0 and table[i][j - 1] == 1: # Left
                    wall += 1
                if j < cols - 1 and table[i][j + 1] == 1: # Right
                    wall += 1

    return wall

input_values = input("Enter the number of rows and columns with space between them: ")
row, column = map(int, input_values.split())

table = []

for _ in range(row):
    row_input = input(f"Enter 0 or 1 in length of {column} with space between them: ")
    row_values = list(map(int, row_input.split()))
    table.append(row_values)

wall_value = calculate_wall(table)

print("The value of the wall is:", wall_value)
