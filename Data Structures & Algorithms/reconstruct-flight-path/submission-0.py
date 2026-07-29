class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # I'll start by building the directed graph.
        for src, dst in tickets:
            graph[src].append(dst)

        # Reverse sort so I can pop the smallest lexical destination from the end.
        for src in graph:
            graph[src].sort(reverse=True)

        route = []

        def dfs(airport: str) -> None:
            # Now I'm tracking unused outgoing tickets from this airport.
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            # This condition handles the postorder build of the Eulerian path.
            route.append(airport)

        dfs("JFK")
        route.reverse()
        return route