import random, time, copy

width = 60
height = 20

# Create a list for the cells
next_cells = []
 
for x in range(width):
    column = []
    for y in range(height):
        if(random.randint(0, 1) == 0):
            column.append('#') # add a living cell
        else:
            column.append(' ')
    next_cells.append(column)

print(next_cells)

while True:
    print('\n\n\n\n') # separate each step with new lines
    currentCells = copy.deepcopy(next_cells)

    # print current cells