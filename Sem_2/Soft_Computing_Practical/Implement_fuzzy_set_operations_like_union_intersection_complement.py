A = {'x1': 0.2, 'x2': 0.7, 'x3': 0.5}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.9}

union = {x: max(A[x], B[x]) for x in A}

intersection = {x: min(A[x], B[x]) for x in A}

complement_A = {x: 1 - A[x] for x in A}

print("Fuzzy Set A:", A)
print("\nFuzzy Set B:", B)
print("\nUnion (A ∪ B):", union)
print("\nIntersection (A ∩ B):", intersection)
print("\nComplement of A (A′):", complement_A)