class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        if n == 1:
            return 0

        queue = deque()
        visited_states = set()

        for i in range(n):
            start_state = (i, frozenset([i]))
            queue.append((i, frozenset([i]), 0))
            visited_states.add(start_state)

        while queue:
            node, visited, steps = queue.popleft()

            if len(visited) == n:
                return steps

            for neighbor in graph[node]:
                new_visited = visited | {neighbor}
                new_state = (neighbor, frozenset(new_visited))

                if new_state not in visited_states:
                    visited_states.add(new_state)
                    queue.append((neighbor, new_visited, steps + 1))

        return -1
