v = int(input())
adj = [[] for _ in range(v)]

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  adj[x].append(y)
  adj[y].append(x)

for i in range(v):
  print(f"{i}-->", end="")
  for node in adj[i]:
    print(node, end=",")
  print()

