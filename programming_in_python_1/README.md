**Disclaimer: This course focuses on the basics of Python there is little that's interesting or creative here, I'm uploading all assignments for completeness' sake. From assignment 5 onwards the course goes into different libraries, which is the more interesting part, the first 4 are just familiarizing with the language.**

---

**Assignment 1:**

Basic Python operations including variable types, mathematical calculations, formatted output, and user input. 

1. **Variable declaration and formatted output**: Demonstrates the use of different data types (boolean, integer, float, and string) and prints them with formatting (e.g., padding and floating-point precision).

2. **Mathematical operations**: Includes taking four user inputs and performing several calculations such as sums, products, division (both integer and float), modulus, exponentiation, square roots, and a complex equation.

3. **Geometrical calculations**: Calculates the circumference, volume, and wall area of a room based on user-input dimensions. It also estimates the number of windows that can fit on the walls and the amount of paint required.

4. **Simple store calculator**: Simulates an order form for a PC parts store, calculating the total cost of cables, monitors, and keyboards based on the user's input.

---

**Assignment 2:**

Python fundamentals, focusing on control structures like loops and conditionals.

1. **Subscription pricing calculator**: Based on the user’s input for subscription duration, a monthly price is determined. For longer subscriptions, the postal code is used to calculate a discounted rate. Invalid inputs for duration or postal code result in error messages.

2. **Comparison of ones digits**: A loop continuously prompts the user for numbers, comparing their ones digits. If two consecutive numbers differ in the ones place, the loop exits with a message. The process stops when the user inputs 'x'.

3. **Number iteration and analysis**: The user inputs a range of numbers with a start, stop, and step value. The program prints the first five numbers in the sequence, counts the number of even numbers, and calculates the sum of odd numbers within the range.

4. **Pattern generation**: Based on user input for the number of lines, the program prints a box shape made of horizontal and vertical lines. The box's width and height correspond to the number of lines provided, and the structure is validated for minimum dimensions.

---

**Assignment 3:**

Various list, matrix, and dictionary operations in Python.

1. **Matrix creation with diagonal ones**: Prompts the user for the number of rows and columns to create a matrix. The program prints a matrix where the diagonal elements are set to 1 and all other elements are 0. The matrix is displayed with row and column headers for better readability.

2. **Element collection and uniqueness check**: The program allows the user to input a sequence of elements until they enter 'x'. It stores all elements in a list, then prints the list and a sorted version of the unique elements (using sets to eliminate duplicates).

3. **Word-to-ordinal dictionary**: Takes a comma-separated list of words as input and creates a dictionary where each word is mapped to the sum of the ASCII values of its characters. The dictionary is printed in a "word -> ordinal sum" format.

4. **Separation of numbers and non-numbers**: Processes a comma-separated list of elements, distinguishing between numbers and non-numbers. The numbers are stored in a list, and a dictionary counts their occurrences. The program also prints the non-numbers as a separate list.

---

**Assignment 4:**

Utility functions, solving specific computational tasks such as list manipulation, data clipping, grade calculation, rounding, and sorting.

1. **Splitting a list into sublists**: A function `split_list` is provided, which takes a list and divides it into a specified number of sublists. The elements are distributed evenly among the sublists in a round-robin fashion.

2. **Value clipping**: The function `clip` takes multiple values and restricts each one to fall within a specified range (default: 0 to 1). Values less than the minimum are set to the minimum, and values greater than the maximum are set to the maximum.

3. **Grade calculator**: This function calculates a student's grade based on a list of assignments, an optional bonus assignment, and the exam score. It checks for several failure conditions such as insufficient exam scores, too many failed assignments, or an overall grade below the passing threshold. The final grade is determined based on percentage thresholds, and the result is returned as a tuple indicating whether the student passed and their grade.

4. **Custom rounding function**: The `round_` function imitates Python’s built-in `round()`, rounding a floating-point number to a specified number of decimal places. It manually checks the digits and adjusts the result accordingly, taking into account cases where no rounding digits are specified.

5. **Sorting function**: A basic sorting algorithm is implemented, which sorts a list of elements in either ascending or descending order. The sorting is done using a variation of the insertion sort algorithm, where elements are swapped based on the desired order.

---

**Assignment 5:**

Recursion, file system navigation, and generator functions.

1. **Recursive list summarization**: The `sub_summarize` function recursively processes a nested list of integers, calculating the sum of all elements. For every sublist encountered, the sum of that sublist is stored in a separate `sub_sums` list. This approach allows for the cumulative sum of both individual sublists and the entire structure.

2. **Directory printing function**: The `print_directory` function recursively prints the contents of a directory in a tree-like structure. It lists files and subdirectories with increasing indentation based on their depth within the directory. The function handles potential errors such as invalid paths or when the path provided points to a file instead of a directory.

3. **Fibonacci sequence generator**: The `gen_fibonacci` function generates Fibonacci numbers up to a specified upper bound using a generator. The function includes error handling for incorrect input types and values. It yields Fibonacci numbers one by one until the specified limit is reached.

---

**Assignment 6:**

File handling, chunk processing, CSV manipulation, and user data management using pickling. 

1. **File Statistics**: The `file_statistics` function reads a text file and computes its basic statistics, such as the number of lines, words, characters, and digits. It also handles errors for invalid paths and non-text files.

2. **File Chunk Generator**: The `chunks` function reads a file in fixed-size chunks, specified by the user, and yields these chunks as output. It handles potential errors, such as invalid file paths or chunk sizes less than 1.

3. **CSV File Merger**: The `merge_csv_files` function merges multiple CSV files based on their columns. It allows merging by either all columns or only shared columns between the files. The result is saved as a new CSV file. This task assumes all files are in the same directory.

4. **User Management with Pickling**: The functions `create_user`, `login`, and `change_password` manage user data stored as serialized (pickled) `.pkl` files. The operations include creating users, logging in, and changing passwords, with a log of each action saved to a text file (`logs.txt`).

---

**Assignment 7:**

Object-oriented programming (OOP) concepts, class hierarchies, inheritance, method overriding, and distance calculations. Defining and manipulating classes to perform mathematical operations.

1. **Radian Class**: The `Radian` class converts an angle in degrees to radians. It uses a method `rad` to compute the radian value, and the `print` method displays both the degree and radian values in a formatted way.

2. **Distance Class**: The `Distance` class serves as an abstract base class for calculating distance. It contains an unimplemented method `dist`, which subclasses are expected to override. The `to_string` method returns a string representation of the class.

3. **Minkowski Distance Class**: The `Minkowski` class is a subclass of `Distance`. It calculates the Minkowski distance between two vectors using the formula for Euclidean distance (`p = 2`). It overrides the `dist` method to perform the calculation and also customizes the `to_string` method to include vector details.

4. **Manhattan Distance Class**: The `Manhattan` class is another subclass of `Distance`. It calculates the Manhattan distance between two vectors (sum of absolute differences). It overrides the `dist` method to perform the calculation and uses the `to_string` method similarly to `Minkowski`.

5. **Euclidean Distance Class**: The `Euclidean` class inherits from `Minkowski` and defaults to calculating Euclidean distance (Minkowski distance with `p=2`). It does not need to redefine the `dist` method because Euclidean distance is a special case of Minkowski distance.

---

**Assignment 8:**

Creation of classes that implement mathematical concepts such as angles, powers, and data scaling. Using object-oriented programming by utilizing special methods (`__init__`, `__add__`, `__call__`, etc.) and applying basic numerical transformations.

1. **Angle Class**: The `Angle` class allows conversions between degrees and radians. It ensures consistency between these two measurements, supports addition of angles, and provides string representations.

2. **Power and Square Classes**: The `Power` class represents an exponent function that can raise a number to a specific power. The `Square` class is a specialized version that defaults to squaring a number.

3. **StandardScaler Class**: The `StandardScaler` class scales features (numeric data) by normalizing them based on mean (`mu`) and standard deviation (`sig`). It supports fitting data, transforming it, and accessing these statistics via indexing.

--- 

**Assignment 9:**

Handling text processing, regular expressions, multiprocessing, and system-level command execution.

1. **Pattern Matching in a File**: This script allows the user to input a file name, character encoding, and a pattern for searching within the file's contents. It searches for all occurrences of the specified pattern using regular expressions.

2. **Email Extraction from Text**: A function that extracts valid email addresses from a given text string using a regular expression pattern that matches typical email formats.

3. **Parallel Summation of Fractions**: This script uses the `multiprocessing` module to divide the task of summing the harmonic series across multiple processes. The result is used to approximate the Euler-Mascheroni constant.

4. **Program Execution with Timeout**: A script that runs a specified program with optional arguments and a timeout. It uses the `subprocess` module to execute the program and capture its output, handling both standard output and errors, with a timeout feature to prevent long-running processes.

---

Here’s the description of **Assignment 10**:

---

 **Assignment 10:**

Array manipulations and numerical operations using NumPy.

1. **Array Extension**: A function that extends a 2D NumPy array to specified dimensions by filling new elements either with specified values or calculated row/column means. The function handles edge cases such as invalid dimensions or incompatible data types.

2. **Element-wise Function Application**: A function that applies a given function element-wise to all elements in a NumPy array, modifying the array in place.

3. **One-hot Encoding**: A function that converts a 1D array of categorical data into a one-hot encoded 2D array. The function raises errors if the input is not 1D or if the array contains incompatible data.

4. **2D Moving Average**: A function that computes the moving average over a sliding window on a 2D numerical array. The window size must be within the bounds of the array's dimensions, and the function raises errors for invalid window sizes or incompatible data types.

---


