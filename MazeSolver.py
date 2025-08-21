# 21.08.2025

maze1 = [
    [0,0,0,0,0],
    [0,'S',1,1,0],
    [0,0,1,'E',0],
    [0,0,0,0,0]
]

maze2 = [
    [0,0,0,0,0,0,0],
    [0,'S',1,1,0,1,0],
    [0,0,0,1,0,1,0],
    [0,1,1,1,1,1,0],
    [0,1,0,0,0,'E',0],
    [0,0,0,0,0,0,0]
]

maze3 = [
    [0,0,0,0,0,0,0,0,0],
    [0,'S',1,0,1,1,1,1,0],
    [0,1,1,0,1,0,0,1,0],
    [0,0,1,1,1,0,1,1,0],
    [0,1,0,0,1,1,1,0,0],
    [0,1,1,1,0,0,'E',0,0],
    [0,0,0,0,0,0,0,0,0]
]

maze4 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,'S',1,1,1,0,1,1,1,0],
    [0,0,0,0,1,0,1,0,1,0],
    [0,1,1,0,1,1,1,0,1,0],
    [0,1,0,0,0,0,1,0,1,0],
    [0,1,1,1,1,1,1,0,'E',0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

maze5 = [
    [0,0,0,0,0,0,0],
    [0,'S',1,1,1,1,0],
    [0,0,0,0,1,0,0],
    [0,1,1,0,1,1,0],
    [0,1,0,0,0,'E',0],
    [0,0,0,0,0,0,0]
]


# מדפיס את המבוך
def print_Maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if j == len(maze[i]) - 1:
                print(maze[i][j])
            else:
                print(maze[i][j], end=" ")

# מוצא את נקודת ההתחלה 'S'
def findStart(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                return (row, col)
    return False

# מוצא את נקודת הסיום 'E'
def findEnd(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'E':
                return (row, col)
    return False

# סימון ביקור
def mark_visited(row, col, visited):
    if (row, col) in visited:
        return False
    visited.add((row, col))
    return True

# בדיקה אם הנקודה בתוך הגבולות
def in_bounds(row, col, maze):
    rows = len(maze)
    cols = len(maze[0])
    return 0 <= row < rows and 0 <= col < cols

# בדיקה אם התא עביר (1, S, E)
def is_passable(cell):
    return cell == 1 or cell == 'S' or cell == 'E'

# אלגוריתם חיפוש לעומק (DFS) עם רקורסיה
def DFS(current_row, current_col, maze_End, maze, visited):
    # למעלה, למטה, ימין, שמאל
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if (current_row, current_col) == maze_End:
        return True
    else:
        for row_change, col_change in directions:
            next_row = current_row + row_change
            next_col = current_col + col_change

            if in_bounds(next_row, next_col, maze):
                if is_passable(maze[next_row][next_col]):
                    if (next_row, next_col) not in visited:
                        mark_visited(next_row, next_col, visited)
                        if DFS(next_row, next_col, maze_End, maze, visited):
                            if maze[current_row][current_col] not in ('S', 'E'):
                                maze[current_row][current_col] = '*'
                            return True
        return False

# פונקציה ראשית לפתרון
def solve_maze_dfs(maze, visited):
    maze_Start = findStart(maze)
    maze_End = findEnd(maze)

    current_row = maze_Start[0]
    current_col = maze_Start[1]

    # סימון ביקור בהתחלה
    mark_visited(current_row, current_col, visited)

    DFS(current_row, current_col, maze_End, maze, visited)

    return maze


def main():
    print("Choose your maze (1 2 3 4 5)")
    maze_choice = input("Choose here: ")

    if maze_choice == "1":
        maze = maze1
    elif maze_choice == "2":
        maze = maze2
    elif maze_choice == "3":
        maze = maze3
    elif maze_choice == "4":
        maze = maze4
    elif maze_choice == "5":
        maze = maze5
    else:
        print("Invalid choice, defaulting to maze1")
        maze = maze1

    visited = set()
    print("Before:")
    print_Maze(maze)
    print("-------------------------------------------------")
    SolvedMaze = solve_maze_dfs(maze, visited)
    print("After:")
    print_Maze(SolvedMaze)

if __name__ == "__main__":
    main()
