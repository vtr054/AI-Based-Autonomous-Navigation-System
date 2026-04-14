import heapq

class PathPlanner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def heuristic(self, p1, p2):
        """Manhattan distance heuristic."""
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def get_neighbors(self, node, grid_data):
        """Returns valid walking directions (Up, Down, Left, Right)."""
        neighbors = []
        r, c = node
        
        # Check directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if grid_data[nr][nc] == 0: # 0 means walkable
                    neighbors.append((nr, nc))
        return neighbors

    def find_path(self, grid_data, start, end):
        """
        Implementation of A* Search Algorithm.
        Returns a list of tuples (row, col) representing the path.
        """
        open_set = []
        heapq.heappush(open_set, (0, start))
        
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        
        open_set_hash = {start}

        while open_set:
            current = heapq.heappop(open_set)[1]
            open_set_hash.remove(current)

            if current == end:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current, grid_data):
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.heuristic(neighbor, end)
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)

        return None # No path found

    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        return path[::-1]
