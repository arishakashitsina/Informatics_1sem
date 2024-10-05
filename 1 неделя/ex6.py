import numpy as np

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    a, b = np.polyfit(x, y, 1)
    return a, b

n = int(input())
x = [0] * n
s = list(input().split())
for i in range(n):
    x[i] = float(s[i])
s = list(input().split())
y = [0] * n
for i in range(n):
    y[i] = float(s[i])
a, b = mnk(x, y)
print(a, b)
