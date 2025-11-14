s1 = {1, 2, 4, 0}
s1.add(-1)
print(s1)

# Frozen sets - Immutable sets
fs1 = frozenset({10, 20, 30})
print(fs1, type(fs1))

fs2 = frozenset({10, 20, 30})
print(fs2, type(fs2))

print(fs1 | fs2)