from collections import deque

def bfs(source, adj, v1):
    q = deque()
    v = v1
    c=0
    visited = [False] * v
    q.append(source)
    visited[source] = True

    while q:
        f = q.popleft()
        c+=1

        for nums in adj[f]:
            if not visited[nums]:
                q.append(nums)
                visited[nums] = True

v = int(input())
adj = [[] for _ in range(v)]

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  adj[x].append(y)
  adj[y].append(x)

# for i in range(v):
#   print(f"{i}-->", end="")
#   for node in adj[i]:
#     print(node, end=",")
#   print()

c=bfs(0,adj,v)

if c == v:
        print("True")
else:
        print("False")
