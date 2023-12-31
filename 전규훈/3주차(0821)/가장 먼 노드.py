def bfs(G, v, n):
    visited = [0] * (n + 1)
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        t = queue.pop(0)
        for w in G[t]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[t] + 1  # 이전 노드의 거리 + 1 ==> 가장 멀리 떨어진 노드의 거리를 구할 수 있다.

    max_v = max(visited)  # 가장 긴 거리 확인(가장 멀리 떨어진 노드의 거리를 구하기 위함)
    cnt = 0  # 가장 멀리 떨어진 노드의 개수
    for i in visited:
        if max_v == i:
            cnt += 1

    return cnt


def solution(n, edge):
    graphs = {}  # 그래프 인접리스트 생성
    for key, value in edge:
        # 정방향 연결
        if key not in graphs.keys():
            graphs.update({key: [value]})
        else:
            graphs[key].append(value)
        # 역방향 연결
        if value not in graphs.keys():
            graphs.update({value: [key]})
        else:
            graphs[value].append(key)

    return bfs(graphs, 1, n)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))