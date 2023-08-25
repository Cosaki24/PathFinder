import ast  # To convert string input into list.
import sys

# Colours.
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def str_to_list(string_to_be_converted):
    '''
    This function converts a string to a list
    '''
    try:
        resulting_list = ast.literal_eval(string_to_be_converted) # convert the input string into a list.
        if isinstance(resulting_list, list):
            print('\n\tCongrats, You now have a grid!\n')
            return resulting_list
        else:
            print(RED + f"\tYour input was {string_to_be_converted}. Do you think you wrote it correctly?" + RESET)
            string_to_be_converted = input("\tTry again!>>>")
            str_to_list(string_to_be_converted)

    except (SyntaxError, ValueError):
        print(RED + f"\tYour input was \"{string_to_be_converted}\". Do you think you wrote it correctly?" + RESET)
        string_to_be_converted = input("\tTry again!>>>")
        str_to_list(string_to_be_converted)

def grid_maker():
    '''
    This function accepts a grid as a list
    from the standard input
    '''
    grid_input = input('''
        Now the grid part!
        Tip: Your grid should always start with a
        Square Bracket [] and should be rectangle.
        I'm assuming you know Maths and Matrices so it
        shouldn't be a problem. (Look at the example grid)
        (Press Enter key to skip and use the example grid)           
        >>> 
            ''')

    if grid_input:
        grid = str_to_list(grid_input)
        return grid   
    else:
        print("\tSo you're lazy, huh? That's OK. You will be using the default grid")
        grid = [
            ['A', '.', '.'],
            ['.', '.', 'B']
        ]
        return grid

def print_nested_grid(grid):
    '''
    This function prints a nested grid 
    in a rectangular format, one that
    is easy to understand and read.
    '''
    for row in grid:
        for cell in row:
            print(YELLOW + '\t', cell, end=' ' + RESET)
        print()


def find_start_point(grid, start_point='A'):
    '''
    This is the genius part of the robot.
    It finds the starting point from anywhere
    in the grid. Yo ho ho ho ho!
    '''
    for row, column in enumerate(grid):
        if start_point in column:
            return row, column.index(start_point)
    return None


def is_valid_move(grid, x, y):
    '''
    Another genius part but a very required one.
    The robot will neither run wild (Go out of grid)
    nor collide with obstacles('X').
    '''
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X'

def obstacles_count(grid, obstacle = 'X'):
    '''
    Finds the number of obstacles in the given grid
    '''
    count = 0
    for row in grid:
        for obstacle in row:
            if obstacle == 'X':
                count += 1
    return count


def knight_mode(grid, current_point, visited):
    '''
    This function directs the robot to find all paths in 
    the grid from A to B making sure it touches all points
    before reaching B.
    '''
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    obstacles = obstacles_count(grid)

    # Checks if the destination 'B' is reached and all points are covered.
    if len(visited) == (len(grid) * len(grid[0]) - obstacles) and grid[current_point[0]][current_point[1]] == 'B':
        return [[current_point]]

    all_paths = []

    # movements and new positions.
    for dx, dy in directions:
        new_x, new_y = current_point[0] + dx, current_point[1] + dy # new point after movement
        if is_valid_move(grid, new_x, new_y) and (new_x, new_y) not in visited: # checks valid move and if the point is already visited
            visited.add((new_x, new_y)) # add new point to a list of visited points.
            paths = knight_mode(grid, (new_x, new_y), visited) # do what this function actualy does.
            for path in paths:
                all_paths.append([current_point] + path) # add new paths to a list of paths
            visited.remove((new_x, new_y))  # remove visited points.

    return all_paths

def basic_mode(grid, current_point, visited):
    '''
    This function directs the robot to find all paths in 
    the grid from A to B. Any paths.
    '''
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    # Checks if the destination 'B' is reached
    if grid[current_point[0]][current_point[1]] == 'B':
        return [[current_point]]

    all_paths = []

    # movements and new positions.
    for dx, dy in directions:
        new_x, new_y = current_point[0] + dx, current_point[1] + dy # new point after movement
        if is_valid_move(grid, new_x, new_y) and (new_x, new_y) not in visited: # checks valid move and if the point is already visited
            visited.add((new_x, new_y)) # add new point to a list of visited points.
            paths = basic_mode(grid, (new_x, new_y), visited) # do what this function actualy does.
            for path in paths:
                all_paths.append([current_point] + path) # add new paths to a list of paths
            visited.remove((new_x, new_y))  # remove visited points.

    return all_paths



print(RED + '''
                ==========Path-Finder========
      ''' + RESET)
print(RED +'''
                ========By Collins Kipepe=====
      ''' + RESET)
print('''
        A robot starts on point marked 'A' on a rectangular grid of points.
        The starting point is always the top left point on the grid (but this robot
        is genius. The starting point can be anywhere). The robot can move left, right,
        up or down, moving from one point to the next. By moving in steps going 
        left, right, up or down, the robot would like to reach a point marked 'B',
        which is always the bottom right point in the grid.( Due to the robot's 
        the end could also be anywhere.)
      
        Sometimes, points are marked as 'X', and the robot is not allowed to visit
        them at all. A robot is never allowed to visit a point more than once.
      
        In how many ways can the robot move from A to B and visit all points along 
        the way?
      
        For example, in the following represented as a nested list 
                    [['A', '.', '.'], ['.', '.', 'B']]
      
                        A   .   .
                        .   .   B
      
        There is only one path from A to B (From A down, right, up, right, down(B)).
      
        Update: While trying this robot, I found out there won't be too many simple
                grids that will have more than one path that touches all points. So to make
                this program more fun, I will include two modes. One that will find a path 
                that touches all points(KNIGHT Mode) and one that will find a paths will 
                reach point 'B' whether it touches all points or not. I will call it the BASIC Mode. 
      
        Now that you are aware how the program works, you will provide a rectangular grid.
        If you don't provide one, the above grid (example) will be used.
        Check out how this Robot is POWERFUL!
      
        By the way, how should I call this Robot? Anyways, I'll give you the
        privilege to do so. Good luck!
      ''')

robot_name = input('\tHow would you like to name this robot?\n\t>>>')
while not robot_name:
    robot_name = input(RED + '\tTake this seriously! Give this robot a name.\n\t>>>' + RESET)

status = True

while status:
    print('''
            Choose the robot mode:
            1. Knight Mode
            2. Basic Mode
            Q. I've had enough. I'm no longer interested. I quit!
        
        ''')

    robot_mode = input('\t>>>')

    if robot_mode == '1':
        print("\n\tKnight Mode")
        grid = grid_maker()
        print("\tHere's is your grid\n")
        print_nested_grid(grid)
        print("\n")
        obstacles = obstacles_count(grid)
        print(BLUE + f"\tThere are {obstacles} obstacle(s)\n" + RESET)
        start_point = find_start_point(grid)
        visited = {start_point}
        all_paths = knight_mode(grid, start_point, visited)
    elif robot_mode == '2':
        print("\n\tBasic Mode\n")
        grid = grid_maker()
        print("\tHere's is your grid\n")
        print_nested_grid(grid)
        print("\n")
        obstacles = obstacles_count(grid)
        print(BLUE + f"\tThere are {obstacles} obstacle(s)\n" + RESET)
        start_point = find_start_point(grid)
        visited = {start_point}
        all_paths = basic_mode(grid, start_point, visited)
    elif robot_mode == 'Q' or robot_mode == 'q':
        sys.exit("\n\tExiting Program. Bye!")
    else:
        sys.exit("\n\tSince you are illiterate, I'll also quit!")    


    if all_paths:
        print(GREEN + f"\tYo ho ho ho! {robot_name} has found {len(all_paths)} path(s)" + RESET)
        print(GREEN +'''
        Assuming you know the basics of Geometry, you can
        understand the syntax of this movement. If you don't,
        Then use 'Pathfinder for Dummies' or Send me an email
               at collysam20@gmail.com.
            ''' + RESET)
        for index, path in enumerate(all_paths):
            print(GREEN + f'\tPath {index + 1}:', path)
            print("\n" + RESET)
    else:
        print(RED + f"\tSorry, {robot_name} has not found any path" + RESET)

    try_again = input("\n\tWant to try again? (y/n): ")

    if try_again == 'n':
        sys.exit("\n\tProgram is exiting")
    elif try_again != 'y':
        sys.exit("\n\tSince you are illiterate, I'll also exit.")
