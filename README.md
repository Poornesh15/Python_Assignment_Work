

# Surrounded Regions Solver

This Python program solves the problem of capturing surrounded regions in a 2D board containing 'X' and 'O'. It utilizes Depth-First Search (DFS) to identify and mark regions that are not surrounded by 'X'.

## Problem Description

Given a 2D board containing 'X' and 'O', our task is to capture all regions surrounded by 'X'. A region is considered surrounded by 'X' if there are 'X' cells surrounding it in all four directions (up, down, left, and right).

## Approach Overview

1. **Depth-First Search (DFS)**: We perform a DFS traversal starting from every 'O' cell along the border of the board.
2. **Marking Cells**: During DFS traversal, we mark cells reachable from the border as '$', indicating they are not surrounded by 'X'.
3. **Converting Cells**: After DFS traversal, we iterate through the board and:
   - Change all remaining 'O' cells to 'X' since they are surrounded by 'X'.
   - Change marked '$' cells back to 'O' as they are not surrounded by 'X'.

    ```

## Inputs

- **Board**: A 2D list representing the board with dimensions `rows` x `cols`.
  - Each cell of the board contains either 'X' or 'O'.

## Outputs

- **Updated Board**: The board with captured regions.
  - All regions surrounded by 'X' remain unchanged.
  - All regions not surrounded by 'X' (reachable from the border) are marked as 'O'.

## Time and Space Complexity

- **Time Complexity**: O(rows * cols) where `rows` and `cols` are the dimensions of the board.
- **Space Complexity**: O(rows * cols) in the worst case.

## Example

Consider the following input board:

```
[
  ['X', 'X', 'X', 'X'],
  ['X', 'O', 'O', 'X'],
  ['X', 'X', 'O', 'X'],
  ['X', 'O', 'X', 'X']
]
```

The output board after processing should be:

```
[
  ['X', 'X', 'X', 'X'],
  ['X', 'X', 'X', 'X'],
  ['X', 'X', 'X', 'X'],
  ['X', 'O', 'X', 'X']
]
```
