import sys

import numpy as np


def read_matrix(filename):
    with open(filename, "r") as f:
        first_line = f.readline().split()
    if len(first_line) == 2:
        rows, cols = map(int, first_line)
    else:
        raise ValueError(
            "First line of the file must contain two integers: number of rows and columns."
        )

    matrix = np.loadtxt(filename, skiprows=1, max_rows=rows, dtype=np.float64)
    return matrix


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python verify.py <first_matrix_file> <second_matrix_file> <result_matrix_file>"
        )
        sys.exit(1)

    first_matrix_file = sys.argv[1]
    second_matrix_file = sys.argv[2]
    result_matrix_file = sys.argv[3]

    try:
        first_matrix = read_matrix(first_matrix_file)
        second_matrix = read_matrix(second_matrix_file)
        result_matrix = read_matrix(result_matrix_file)
        expected_result = np.dot(first_matrix, second_matrix)

        if np.allclose(result_matrix, expected_result, rtol=1e-5, atol=1e-8):
            print("Verification successful!")
            sys.exit(0)
        else:
            print("Verification failed!")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
