import numpy as np
import numbers

def extend(arr: np.ndarray, rows: int, cols: int, fill=None) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f'can only extend 2D arrays, not {arr.ndim}D')
    arr_rows = arr.shape[0]
    if rows < arr_rows:
        raise ValueError("invalid rows")
    arr_cols = arr.shape[1]
    if cols < arr_cols:
        raise ValueError("invalid cols")
    if fill is not None and not isinstance(fill,  numbers.Number):
        raise ValueError("invalid fill")

    if (arr_rows, arr_cols) == (rows, cols):
        array = np.copy(arr)
    else:
        array = np.empty((rows, cols), dtype=arr.dtype)
        array[:arr_rows, :arr_cols] = arr

        if fill is None:
            row_means = np.mean(arr, axis=1)
            col_means = np.mean(arr, axis=0)
            total_mean = np.mean(arr)

            for i in range(rows):
                for j in range(cols):
                    if i >= arr_rows and j >= arr_cols:
                        array[i, j] = total_mean
                    elif i >= arr_rows:
                        array[i, j] = col_means[j]
                    elif j >= arr_cols:
                        array[i, j] = row_means[i]
        else:
            if rows > arr_rows:
                array[arr_rows:, :] = fill
            if cols > arr_cols:
                array[:, arr_cols:] = fill

    return array

# m1 = np.arange(2*3).reshape(2,-1)
# print(m1)
# print(extend(m1, 2, 3))
# print(extend(m1, 4, 5))

# try:
#     print(extend(m1, 2, 1))
# except ValueError as e:
#     print(f"ValueError: {e}")
# try:
#     print(extend(m1, 1, 2))
# except ValueError as e:
#     print(f"ValueError: {e}")

# m2 = np.arange(2*3,dtype=float).reshape(2,-1)
# print(m2)
# print(extend(m2, 4, 5))
# print(extend(m1, 4, 5, fill=10))

# try:
#     print(extend(m2, 4,4, fill="foo"))
# except ValueError as e:
#     print(f"ValueError: {e}")
# m3 = np.ones(1)
# print(m3)
# try:
#     print(extend(m3, 2, 3))
# except ValueError as e:
#     print(f"ValueError: {e}")
