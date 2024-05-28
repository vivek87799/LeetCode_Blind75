def pad_matrix(matrix):
    # Determine the dimensions of the original matrix
    m, n = len(matrix), len(matrix[0])

    # Pad the matrix with zeros on all sides
    padded_matrix = [[0] * (n + 2) for _ in range(m + 2)]
    for i in range(m):
        for j in range(n):
            padded_matrix[i+1][j+1] = matrix[i][j]

    return padded_matrix

def slide_window(matrix):
    
    target_index=0
    # Define the sliding window pattern
    window_pattern = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

    # Pad the matrix
    padded_matrix = pad_matrix(matrix)

    # Initialize the result matrix and indices list
    result = []
    indices_list = []
    traced_path = []
    i=1
    # Slide the window across the padded matrix
    while i < len(padded_matrix)-1:
    # for i in range(1, len(padded_matrix) - 1):
        row = []
        indices_row = []
        j=1
        while j < len(padded_matrix[0])-1:
        # for j in range(1, len(padded_matrix[0]) - 1):
            # Extract the submatrix corresponding to the current window position
            submatrix = [padded_matrix[i - 1][j - 1:j + 2],
                         padded_matrix[i][j - 1:j + 2],
                         padded_matrix[i + 1][j - 1:j + 2]]

            # Apply the window pattern and sum the elements
            # Filtered window search area
            
            window_search_area = [submatrix[k][l] 
                      for k in range(3) 
                      for l in range(3) 
                      if window_pattern[k][l] == 1 
                      and 
                      (k, l) not in traced_path]
            print(window_search_area)

            print("traced path", traced_path)
            
            
            """
            window_search_area = [submatrix[k][l] 
                                  for k in range(3) 
                                  for l in range(3)
                                  if window_pattern[k][l] == 1]
            """
            window_sum = targets[target_index] in window_search_area
            print(window_search_area, window_sum, targets[target_index])

            # Store the result
            row.append(window_sum)

            # Store the indices where the target exists (if true)
            if window_sum:
                
                indices = [(i - 1 + k, j - 1 + l) for k in range(3) for l in range(3) if submatrix[k][l] * window_pattern[k][l]  == targets[target_index]]
                indices_row.append(indices)
                traced_path.append(indices)
                target_index+=1
                # print(window_search_area, indices)
            else:
                indices_row.append([])
            if target_index > len(targets)-1:
                result.append(row)
                indices_list.append(indices_row)
                traced_path.append(indices_row)
                return result, indices_list
            if window_sum:
                print(indices[0])
                i, j = indices[0]
            elif traced_path:
                traced_path.pop()
                i,j=traced_path[-1][0]
            else:
                j+=1
                print("traced_path", traced_path)
        result.append(row)
        indices_list.append(indices_row)
        if target_index > len(targets)-1:
            return result, indices_list
        i+=1
    return result, indices_list

target_index = 0
# Example matrix
matrix = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't']
]


targets = ['a', 'f', 'g', 'h', 'm','r', 's', 'n','o', 't', 'o', 'n', 'c'] 


# Slide the window over the matrix
result, indices_list = slide_window(matrix)
print("Boolean Matrix:")
for row in result:
    print(row)

print("\nIndices List:")
for indices_row in indices_list:
    print(indices_row)

