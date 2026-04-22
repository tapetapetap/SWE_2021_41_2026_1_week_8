# main.py (main 브랜치용 뼈대 코드)
from typing import List

def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    """
    # TODO: Implement even_list
    return [x for x in int_list if x % 2 == 0]

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers.
    """
    # TODO: Implement sum_of_squares_of_even
    pass

def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()