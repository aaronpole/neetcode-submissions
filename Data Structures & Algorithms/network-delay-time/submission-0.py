class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visit = set()
        t = 0

        while minHeap:
            time_now, node_1 = heapq.heappop(minHeap)
            if node_1 in visit:
                continue
            visit.add(node_1)
            t = time_now

            for node_2, time_next in edges[node_1]:
                if node_2 not in visit:
                    heapq.heappush(minHeap, (time_now + time_next, node_2))
        return t if len(visit) == n else -1