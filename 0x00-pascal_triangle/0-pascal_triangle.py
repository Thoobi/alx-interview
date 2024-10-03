def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    triangle = []  # Initialize the list to hold the triangle

    for i in range(n):
        # Start each row with a list containing 1
        row = [1] * (i + 1)
        
        # Each element (except the first and last) is the sum of the two elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)  # Add the current row to the triangle
    
    return triangle
