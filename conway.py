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
    try:
        print('\n\n\n\n') # separate each step with new lines
        current_cells = copy.deepcopy(next_cells) # copy the cells

        # print current cells
        for y in range(height):
            for x in range(width):
                print(current_cells[x][y], end='')
            print()
        
        # Calculate the next step's cells based on current step's cells:
        for x in range(width):
            for y in range(height):
                left_coord = (x - 1) % width # the modulus operator makes sure the coord is with the width and height range always
                right_coord = (x + 1) % width
                above_coord = (y + 1) % height
                below_coord = (y - 1) % height

                num_of_living_neighbours = 0
                # Use mutliple if statements to check the living status of the cells
                if (current_cells[left_coord][y] == '#'):
                    num_of_living_neighbours += 1 # cell to the left is alive
                if (current_cells[right_coord][y] == '#'):
                    num_of_living_neighbours += 1 # cell to the right is alive
                if (current_cells[x][above_coord] == '#'):
                    num_of_living_neighbours += 1 # cell above is alive
                if (current_cells[x][below_coord] == '#'):
                    num_of_living_neighbours += 1 # cell below is alive
                if (current_cells[right_coord][above_coord] == '#'):
                    num_of_living_neighbours += 1 # cell top diagonal to the right is alive
                if (current_cells[right_coord][below_coord] == '#'):
                    num_of_living_neighbours += 1 # cell bottom diagonal to the right is alive
                if (current_cells[left_coord][above_coord] == '#'):
                    num_of_living_neighbours += 1 # cell top diagonal to the left is alive
                if (current_cells[left_coord][below_coord] == '#'):
                    num_of_living_neighbours += 1 # cell bottom diagonal to the left is alive

                if(current_cells[x][y] == '#' and (num_of_living_neighbours == 2 or num_of_living_neighbours == 3)):
                    next_cells[x][y] = '#'
                elif(current_cells[x][y] == ' ' and num_of_living_neighbours == 3):
                    next_cells[x][y] = '#'
                else:
                    next_cells[x][y] = ' '
        time.sleep(1)
    except KeyboardInterrupt:
        print('Done for neow')
        break