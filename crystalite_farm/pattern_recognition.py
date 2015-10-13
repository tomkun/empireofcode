def mark_patterns(pattern, image):
    pattern_len= len(pattern)
    pattern_row_len = len(pattern[0])
    row_len = len(image[0])

    for row in range(len(image)-pattern_len+1):
        for i in range(row_len-pattern_row_len+1):
            if image[row][i] == pattern[0][0]:
                s = subset(image, (row, i), (row+pattern_len, i+pattern_row_len))
                if s == pattern:
                    mark(image, (row, i), pattern_len, pattern_row_len)
    return image

def subset(arr, start, end):
    """
    Takes two endpoints (row,col) and returns a sliced copy of a 2d array.
    Exclusive!
    """
    return [[row_data for row_data in row[start[1]:end[1]]] for row in arr[start[0]:end[0]]]
    
def mark(image, begin, pattern_len, pattern_row_len):
    """
    Performs an in-place modification of the array.
    """
    tab = {1:3, 0:2} ## our replacement table
    for row_idx in range(begin[0], begin[0]+pattern_len):
        for col_idx in range(begin[1], begin[1]+pattern_row_len):
            image[row_idx][col_idx] = tab[image[row_idx][col_idx]]
    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert mark_patterns([[1, 0], [1, 1]],
                         [[0, 1, 0, 1, 0],
                          [0, 1, 1, 0, 0],
                          [1, 0, 1, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                                [0, 3, 3, 0, 0],
                                                [3, 2, 1, 3, 2],
                                                [3, 3, 0, 3, 3],
                                                [0, 1, 1, 0, 0]], "1st"
    assert mark_patterns([[1, 1], [1, 1]],
                         [[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]]) == [[3, 3, 1],
                                          [3, 3, 1],
                                          [1, 1, 1]], "2nd"
    assert mark_patterns([[0, 1, 0], [1, 1, 1]],
                         [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                          [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                          [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                          [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                          [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                               [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                               [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                               [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                               [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                               [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                               [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "3rd"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
