import numpy as np

def moving_average_2D(arr: np.ndarray, size: int) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f"apply for 2D array, not {arr.ndim}D")
    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Invalid data type")
    if size < 1 or size > arr.shape[0] or size > arr.shape[1]:
        raise ValueError("Invalid window size")
    
    rows = arr.shape[0] - size + 1
    cols = arr.shape[1] - size + 1
    array = np.zeros((rows, cols))


    for i in range(rows):
        for j in range(cols):
            window = arr[i:i + size, j:j + size]
            array[i, j] = np.mean(window)

    return array

# arr = np.arange(4*5).reshape(4, -1)
# print(arr)
# result = moving_average_2D(arr, 3)
# print(result)

# try:
#     moving_average_2D(arr, 5)
# except ValueError as e:
#     print(f"ValueError: {e}")

# try:
#     moving_average_2D(np.array([["a", "b"], ["c", "d"]]), 2)
# except TypeError as e:
#     print(f"TypeError: {e}")