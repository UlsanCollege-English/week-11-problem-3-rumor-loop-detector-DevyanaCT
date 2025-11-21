"""
HW03 — Rumor Loop Detector (Cycle in Undirected Graph)

Implement:
- has_cycle(graph)
- find_cycle(graph)
"""

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""
    return find_cycle(graph) is not None


def find_cycle(graph):
    """Return a list of nodes forming a simple cycle where first == last.
    If no cycle, return None.

    - Must use DFS & parent map
    - Self-loop counts: return [u, u]
    """

    visited = set()
    parent = {}

    # Detect and return cycle from DFS recursion
    def dfs(u):
        visited.add(u)

        for v in graph[u]:
            # self-loop case
            if v == u:
                return [u, u]

            if v not in visited:
                parent[v] = u
                cycle = dfs(v)
                if cycle:
                    return cycle
            else:
                # `v` is visited → check if not parent (true cycle)
                if parent.get(u) != v:
                    # reconstruct cycle from u -> ... -> v
                    return reconstruct_cycle(u, v)

        return None

    # Reconstruct a simple cycle from u back to v
    def reconstruct_cycle(u, v):
        path_u = [u]
        path_v = [v]

        # climb up from u and v until they meet
        pu = u
        pv = v

        # to avoid infinite loops, track ancestors
        ancestors_u = set([u])

        # build ancestors for u
        while pu in parent:
            pu = parent[pu]
            ancestors_u.add(pu)

        # climb from v to find intersection
        pv = v
        while pv not in ancestors_u:
            pv = parent[pv]
            path_v.append(pv)

        # pv is now LCA (meeting point)
        meeting = pv

        # build path_u from u back to meeting
        pu = u
        path_u = [u]
        while pu != meeting:
            pu = parent[pu]
            path_u.append(pu)

        # full cycle: u → … → meeting → reverse(v → … → meeting)
        path = path_u + path_v[::-1]
        path.append(path[0])  # close the cycle

        return path

    # Loop through all components
    for node in graph:
        if node not in visited:
            parent[node] = None
            cycle = dfs(node)
            if cycle:
                return cycle

    return None
