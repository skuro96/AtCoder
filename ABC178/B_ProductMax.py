a, b, c, d = (int(x) for x in input().split())

maxval = a * c
if a * d > maxval:
    maxval = a * d
if b * c > maxval:
    maxval = b * c
if b * d > maxval:
    maxval = b * d

print(maxval)