python3 <<EOF
matrix = [line[:-1].split(' ') for line in open('file.txt')]
for column in range(len(matrix[0])):
    print(*(matrix[row][column] for row in range(len(matrix))))
EOF
