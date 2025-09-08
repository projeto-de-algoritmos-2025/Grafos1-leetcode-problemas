class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for from_node, to_node in edges:
            tree[from_node].append(to_node)
            tree[to_node].append(from_node)

        result = [0] * n
        count = [0] * n

        def dfs1(u, parent, depth):
            count[u] = 1
            result[0] += depth
            for to_node in tree[u]:
                if to_node != parent:
                    dfs1(to_node, u, depth + 1)
                    count[u] += count[to_node]

        def dfs2(u, parent):
            for to_node in tree[u]:
                if to_node != parent:
                    result[to_node] = result[u] - count[to_node] + (n - count[to_node])
                    dfs2(to_node, u)

        dfs1(0, -1, 0)
        dfs2(0, -1)

        return result