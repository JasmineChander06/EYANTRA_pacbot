import sys
from pathlib import Path

# Allow Python to find files inside the src folder.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from path_planner import shortest_path
from maze_2b import Maze


def main():
    maze = Maze.official()

    start = maze.spawn_cell
    goal = maze.exit_cell

    path = shortest_path(maze, start, goal)

    if not path:
        print("No path found!")
        return

    print("Path found successfully!")
    print("Start:", path[0])
    print("Goal:", path[-1])
    print("Number of cells:", len(path))
    print("Number of moves:", len(path) - 1)
    print("Path:", path)

    # Verify every step follows an open passage.
    for current, next_cell in zip(path, path[1:]):
        valid_move = any(
            neighbour == next_cell
            for _, neighbour in maze.neighbours(current)
        )

        assert valid_move, f"Invalid move: {current} -> {next_cell}"

    print("All moves are valid!")


if __name__ == "__main__":
    main()