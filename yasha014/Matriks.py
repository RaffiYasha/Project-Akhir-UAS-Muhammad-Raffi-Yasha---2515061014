def perkalian_matriks(A, B):
    hasil = []

    for i in range(3):
        baris = []

        for j in range(3):
            jumlah = 0

            for k in range(3):
                jumlah += A[i][k] * B[k][j]

            baris.append(jumlah)

        hasil.append(baris)

    return hasil