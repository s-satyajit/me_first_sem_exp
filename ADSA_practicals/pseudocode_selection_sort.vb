for end from n-1 downto 1:
    max_index = 0
    for j from 1 to end:
        comparisons++
        if A[j] > A[max_index]:
            max_index = j
    if max_index != end:
        swap A[max_index] and A[end]
        swaps++
