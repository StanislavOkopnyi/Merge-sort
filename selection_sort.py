# Сортировка выбором (Selection sort) — алгоритм сортировки.
# Может быть как устойчивый, так и неустойчивый.
# На массиве из n элементов имеет время выполнения в худшем,
# среднем и лучшем случае Θ(n2), предполагая что сравнения делаются за постоянное время.

def find_smallest(arr: list) -> int:
    smallest_elem_ind = 0
    for index in range(1, len(arr)):
        if arr[index] < arr[smallest_elem_ind]:
            smallest_elem_ind = index
    return smallest_elem_ind


def selection_sort(arr: list) -> list:
    result = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        result.append(arr.pop(smallest))
    return result
