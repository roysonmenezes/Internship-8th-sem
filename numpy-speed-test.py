import time
import numpy as np

# Create 1 Million Numbers
size = 1_000_000

# Python List Test
start = time.time()

py_list = list(range(size))
py_result = [x * 2 for x in py_list]

end = time.time()
python_time = end - start

print("Python List Execution Time:", python_time, "seconds")


# NumPy Array Test
start = time.time()

np_array = np.arange(size)
np_result = np_array * 2

end = time.time()
numpy_time = end - start

print("NumPy Array Execution Time:", numpy_time, "seconds")