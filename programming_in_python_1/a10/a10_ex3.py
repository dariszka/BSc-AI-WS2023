import numpy as np 

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError(f"The function can work for 1D matrices, not {arr.ndim}D")
    
    unique_arr = np.unique(arr)
    unique_arr.sort()

    array = np.zeros((len(arr), len(unique_arr)))

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if arr[i] == unique_arr[j]:
                array[i][j] = 1

    return array

# a = np.array(["a", "a", "b", "c"])
# print(one_hot_encoding(a))
# a = np.array([10, 5, 15, 20])
# print(one_hot_encoding(a))
# a = np.array([[1, 2], [3, 4]])
# try:
#     print(one_hot_encoding(a))
# except ValueError as e:
#     print(f"ValueError: {e}")

