# table_sorter.py
# This program asks the user to enter a list of numbers,
# sorts the list, and displays the sorted result.

def bubble_sort(arr):
    n = len(arr)

    # Bubble Sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    print("=== TABLE SORTER ===")
    print("Enter numbers separated by spaces.")
    print("Example: 5 2 9 1 7")

    # Read user input
    user_input = input("Table: ")

    try:
        # Convert input to list of integers
        table = [int(x) for x in user_input.split()]

        # Sort the list
        sorted_table = bubble_sort(table.copy())

        # Display results
        print("\nOriginal table:", table)
        print("Sorted table:  ", sorted_table)

    except ValueError:
        print("Error: Please enter only integers separated by spaces.")


if __name__ == "__main__":
    main()