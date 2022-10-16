a = [0, 1, 4, 3, 7, 9]

m = a[0]
n = a[0]

for i in a:
    if i < m:
        m = i

for i in a:
    if i > n:
        n = i

for x in a:
    if x < n and x != m:
        n = x
print(n)
