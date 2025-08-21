# maze-solver-dfs
Maze solver in Python using DFS algorithm כולל פלט לדוגמא

# Maze Solver in Python (DFS)

A simple maze solver implemented in Python using the **Depth-First Search (DFS)** algorithm.  
The program finds a path from `S` (start) to `E` (exit) and marks it with `*`.

## Run
```bash
python maze_solver.py


example output: 
### Larger Maze Example

**Before**

0 0 0 0 0 0 0 0 0  
0 S 1 0 1 1 1 1 0  
0 1 1 0 1 0 0 1 0  
0 0 1 1 1 0 1 1 0  
0 1 0 0 1 1 1 0 0  
0 1 1 1 0 0 E 0 0  
0 0 0 0 0 0 0 0 0  

**After**

0 0 0 0 0 0 0 0 0  
0 S * 0 1 1 1 1 0  
0 1 * 0 1 0 0 1 0  
0 0 * * * 0 1 1 0  
0 1 0 0 * * * 0 0  
0 1 1 1 0 0 E 0 0  
0 0 0 0 0 0 0 0 0  
