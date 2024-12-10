h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
bir = h1 * 3600 + m1 * 60 + s1
ikki = h2 * 3600 + m2 * 60 + s2

vaqt = ikki - bir

print(vaqt)