mat = []
r1 = int(input("Enter, How many rows are there in your matrix:  "))
c1 = int(input("Enter, How many columns are there in your matrix:  "))
ans = 0
if (r1 != c1):
    print("Sorry, I can't fine determinant of your matrix becouse number of columns and number of rows are not equal.")

else:
    for i in range(0, r1):
        for j in range(0, c1):
            mat.append(int(input(f"Enter the elemant which is at ({i + 1}, {j + 1}):  ")))

ans = ans + mat[0]*(mat[4]*mat[8] - mat[5]*mat[7]) - mat[1]*(mat[3]*mat[8] - mat[5]*mat[6]) + mat[2]*(mat[3]*mat[7] - mat[4]*mat[6])
print(f"The detreminant of the matrix is {ans}")