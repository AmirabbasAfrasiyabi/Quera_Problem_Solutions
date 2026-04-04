n = int(input())
rows = [tuple(map(int, input().split())) for _ in range(n)]

perim = 0

for i in range(n):
    l, r = rows[i]
    length = r - l
    perim += 2 * length + 2
    if i > 0:
        pl, pr = rows[i - 1]  # previous row

        overlap = max(0, min(r, pr) - max(l, pl))

        perim -= 2 * overlap

print(perim)
