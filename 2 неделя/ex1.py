m, s = list(input().split())
m = int(m)
n = len(s)
scur = ""
ans = ""
for i in range(n):
    scur += s[i]
    if (i % m) == m - 1:
        scur = scur[::-1]
        ans += scur
        scur = ""

print(ans)