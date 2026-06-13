import raffi028

A = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

hasil = raffi028.determinan_3x3(A)

print("Matriks:")
for baris in A:
    print(baris)

print("\nDeterminan =", hasil)