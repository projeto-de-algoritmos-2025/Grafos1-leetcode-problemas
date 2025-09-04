class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0] * n

        for from_node, to_node in edges:
            incoming[to_node] += 1

        return [i for i in range(n) if incoming[i] == 0]