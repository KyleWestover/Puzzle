import heapq


# Citation for the following function:
# Date: 07/05/2022
# Adapted from Djikstra's algorithm function:
# Source URL: https://github.com/DURepo/CS_325_Exercises/blob/main/Graph-calculate_distances.py

def solve_puzzle(Board, Source, Destination):
    b_dict = {}
    paths = {}

    # convert Board to dictionary where the current node is the key and the
    # value is a dictionary with all open adjacent nodes as keys and weight
    # value of 1 as the values
    for r in range(len(Board)):
        for c in range(len(Board[0])):
            if Board[r][c] != "#":
                b_dict[(r, c)] = {}
                if c + 1 < len(Board[0]) and Board[r][c+1] != "#":
                    inner_dict = b_dict[(r, c)]
                    inner_dict[(r, c + 1)] = 1
                if c - 1 >= 0 and Board[r][c - 1] != "#":
                    inner_dict = b_dict[(r, c)]
                    inner_dict[(r, c - 1)] = 1
                if r + 1 < len(Board) and Board[r + 1][c] != "#":
                    inner_dict = b_dict[(r, c)]
                    inner_dict[(r + 1, c)] = 1
                if r - 1 >= 0 and Board[r - 1][c] != "#":
                    inner_dict = b_dict[(r, c)]
                    inner_dict[(r - 1, c)] = 1

    distances = {vertex: float('infinity') for vertex in b_dict}
    distances[Source] = 0

    pq = [(0, Source)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in b_dict[current_vertex].items():
            distance = current_distance + weight

            # record locally shortest paths for each vertex
            if current_vertex not in paths:
                paths[current_vertex] = [neighbor]
            else:
                paths[current_vertex].append(neighbor)

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # work backwards from Destination to Source, choosing the neighbor node
    # with shortest distance from Source at each step
    tracker = Destination
    result = [Destination]
    directions = ''
    while tracker != Source:
        min_dist = 999999
        min_coord = tracker
        if tracker not in paths:
            return None
        for n in paths[tracker]:
            if distances[n] < min_dist:
                min_dist = distances[n]
                min_coord = n
        result.append(min_coord)

        # create backwards direction string
        (m, n) = min_coord
        (x, y) = tracker
        if m - x > 0:
            directions += 'U'
        elif x - m > 0:
            directions += 'D'
        elif n - y > 0:
            directions += 'L'
        elif y - n > 0:
            directions += 'R'

        tracker = min_coord

    # reverse path result list and directions string, then add both to final
    # and return
    result.reverse()
    final_directions = directions [::-1]
    final = [result, final_directions]
    return final
