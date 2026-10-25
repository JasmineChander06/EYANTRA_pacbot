import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from maze_2b import Maze
from pellet_planner import plan_pellet_route


def main():
    maze = Maze.official()

    start = maze.spawn_cell
    pellets = [(13, 1), (12, 5), (10, 12)]
    exit_cell = maze.exit_cell

    route = plan_pellet_route(
        maze,
        start,
        pellets,
        exit_cell
    )

    if not route:
        print("ERROR: No valid route found.")
        return

    print("Pellet route found!")
    print("Start:", route[0])
    print("Exit:", route[-1])
    print("Total moves:", len(route) - 1)
    print("Route:", route)

    for pellet in pellets:
        assert pellet in route, (
            f"Pellet was missed: {pellet}"
        )

    print("All pellets included!")

    for current, next_cell in zip(route, route[1:]):
        neighbours = [
            neighbour
            for heading, neighbour in maze.neighbours(current)
        ]

        assert next_cell in neighbours, (
            f"Invalid move: {current} -> {next_cell}"
        )

    assert route[-1] == exit_cell

    print("All moves are valid!")
    print("Route ends at the exit!")
    print("TEST PASSED!")


if __name__ == "__main__":
    main()