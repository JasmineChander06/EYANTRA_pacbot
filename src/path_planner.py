from collections import deque


def shortest_path(maze, start, goal):
    """
    Find the shortest path between two cells using BFS.

    Args:
        maze: Official Maze object.
        start: Starting cell (row, col).
        goal: Destination cell (row, col).

    Returns:
        A list of cells from start to goal,
        or an empty list if no path exists.
    """

    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for heading, neighbour in maze.neighbours(current):
            if neighbour not in parent:
                parent[neighbour] = current
                queue.append(neighbour)

    if goal not in parent:
        return []

    # Reconstruct the path from goal to start.
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

