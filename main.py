t = int(input())
ruyxat = []
mod = 10**9 + 7
for _ in range(t):
    n = int(input())
    Sn = (n * n) % mod  
    ruyxat.append(Sn)
for son in ruyxat:
    print(son)