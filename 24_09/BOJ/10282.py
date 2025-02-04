from sys import stdin as ss

'''
시간초과
'''


def get_smallest_node():
    min_val = INF
    idx = 0

    for i in range(1, n+1):
        if time_table[i] < min_val and not visited[i]:
            min_val = time_table[i]
            idx = i

    return idx


def dijkstra(node):
    time_table[node] = 0
    visited[node] = 1

    for i in relation[node]:
        time_table[i[0]] = i[1]

    for _ in range(n-1): # 시작 node를 뺀 나머지 node를 순회
        now = get_smallest_node()
        visited[now] = 1

        for j in relation[now]:
            if time_table[now] + j[1] < time_table[j[0]]:
                time_table[j[0]] = time_table[now] + j[1]



tc = int(ss.readline())
INF = 1e9

for _ in range(tc):
    n, d, c = map(int, ss.readline().split())
    relation = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    time_table = [INF] * (n+1)
    cnt = 0
    sec = 0

    for _ in range(d):
        a, b, s = map(int, ss.readline().split())
        relation[b].append((a, s))

    dijkstra(c)

    for i in range(1, n+1):
        if time_table[i] != 1e9:
            cnt += 1
            if time_table[i] > sec:
                sec = time_table[i]

    print(cnt, end=' ')
    print(sec)
