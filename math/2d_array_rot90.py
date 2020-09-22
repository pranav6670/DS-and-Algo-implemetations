

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = len(a)
for r in range(N):
    for c in range(r, N):
        a[r][c], a[c][r] = a[c][r], a[r][c]  # Transpose the matrix

print(a)

for r in range(0, N):
    for c in range(0, N//2):
        a[r][c], a[r][N - 1 - c] = a[r][N - 1 - c], a[r][c]  # Swap columns

print(a)
