import yasha014

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

hasil = raffi028.perkalian_matriks(A, B)

print("Matriks A")
for baris in A:
    print(baris)

print("\nMatriks B")
for baris in B:
    print(baris)

print("\nHasil Perkalian")
for baris in hasil:
    print(baris)