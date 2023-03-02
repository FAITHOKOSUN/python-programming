def matrix_divided(matrix, div):
    mat = []
    for row in matrix:
        if not all(isinstance(x,(int,float))for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        if not  isinstance(div,(int, float)):
            raise TypeError(" div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_matrix = []
        for x in row:
            new_matrix.append(round(x/div, 2))
        mat.append(new_matrix)
    return mat
        
            
         
            
            
             
            