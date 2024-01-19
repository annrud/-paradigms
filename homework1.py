
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return nums


if __name__ == "__main__":
    nums = [5, 2, 8, 1, 3]
    print(sort_list_imperative(nums))
    print(sort_list_declarative(nums))
