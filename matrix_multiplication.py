mat1 = []
mat2 = []
rMat = []
sum = 0

r1 = int(input("How many rows are there in your first matrix:  "))
c1 = int(input("How many columns are there in your first matrix:  "))
r2 = int(input("\nHow many rows are there in your second matrix:  "))
c2 = int(input("How many columns are there in your first matrix:  "))
n = 0

if (c1 != r2):
    print("\n\nSorry!, I cannot multiply your matrix. To multiply two matrices make sure the number of columns of the first matrix is equal to the number of rows of the srcond matrix.")

else:
    print("\n\nEnter the elements of the first matrix.\n")
    for i in range(0, r1):
        for j in range(0, c1):
            mat1.append(int(input(f"Enter the element which is at ({i + 1},{j + 1}):  ")))

    print("\n\nEnter the elements of the second matrix\n")
    for i in range(0, r2):
        for j in range(0, c2):
            mat2.append(int(input(f"Enter the element which is at ({i + 1},{j + 1}):  ")))

    for i in range(0, r1):
        for j in range(0, c2):
            for k in range(0, c1):
                sum = sum + mat1[n]*mat2[j + k*c2]
                n += 1
            n = i*c1
            rMat.append(sum)
            sum = 0
        n += c1
    n = 0
    
    print("\n\nPrinting the element of the final matrix ...\n")
    for i in range(0, r1):
        for j in range(0, c2):
            print(f"The element which is at ({i + 1},{j + 1}) = {rMat[n]}")
            n += 1