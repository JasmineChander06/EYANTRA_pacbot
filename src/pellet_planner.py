from itertools import permutations
from path_planner import shortest_path


def plan_pellet_route(maze, start, pellets, exit_cell):
    best_route = None
    best_distance = float("inf")

    for order in permutations(pellets):
        route = [start]
        current = start
        valid = True

        for pellet in order:
            segment = shortest_path(maze, current, pellet)

            if not segment:
                valid = False
                break

            route.extend(segment[1:])
            current = pellet

        if not valid:
            continue

        segment = shortest_path(maze, current, exit_cell)

        if not segment:
            continue

        route.extend(segment[1:])

        distance = len(route) - 1

        if distance < best_distance:
            best_distance = distance
            best_route = route

    if best_route is None:
        return []

    return best_route

