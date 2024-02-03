# Бинарный поиск
def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1


if __name__ == '__main__':
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_number = 9
    result = binary_search_recursive(
        sorted_array,
        target_number,
        0,
        len(sorted_array) - 1
    )

    if result != -1:
        print(f'Элемент {target_number} найден в массиве. Его индекс: {result}')
    else:
        print(f'Элемент {target_number} не найден в массиве.')
