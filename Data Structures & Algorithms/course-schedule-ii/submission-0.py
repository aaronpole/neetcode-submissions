class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        for src,dst in prerequisites:
            indegree[dst] += 1
            adjList[src].append(dst)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return [] if finish != numCourses else output[::-1]