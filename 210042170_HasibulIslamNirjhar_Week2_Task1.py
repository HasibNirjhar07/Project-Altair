def process_instructions(instructions, grid_size):
  # Defining the initial position and direction
  x, y = 0, 0
  direction = 'N'

  # Storing the value of left and right turns of each direction
  
  left_turns = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
  right_turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

  #Reading the instruction through for loop and executing it
  for instruction in instructions:
    if instruction == 'F':  # Move forward
      if direction == 'N':
        y = min(y + 1, grid_size[1] - 1)  # Move up and only take the min value so that the graph doesnt excede its grid size
      elif direction == 'E':
        x = min(x + 1, grid_size[0] - 1)  # Move right and take the min value
      elif direction == 'S':
        y = max(y - 1, 0)  # Move down so and take the max value so that the grid doesnt go beyond 0,0 grid
      elif direction == 'W':
        x = max(x - 1, 0)  # Move left and take the max value
    elif instruction == 'L':  # Turn left
      direction = left_turns[direction]
    elif instruction == 'R':  # Turn right
      direction = right_turns[direction]

  return x, y, direction


# Test case:
instructions = "FFLFFRFL"
grid_size = (5, 5)
print(process_instructions(instructions, grid_size))