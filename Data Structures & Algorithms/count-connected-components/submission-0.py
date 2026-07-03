class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visted = set()
        def dfs(node):
            if node in visted:
                return
            visted.add(node)
            for e in graph[node]:
                dfs(e)

        
        for i in range(n):
            if i not in visted:
                dfs(i)
                count += 1
        return count