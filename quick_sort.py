# Один из самых быстрых известных универсальных алгоритмов сортировки массивов:
# в среднем O( n log n ) обменов при упорядочении n элементов;
# из-за наличия ряда недостатков на практике обычно используется
# с некоторыми доработками.


def quick_sort(list_to_sort: list) -> list | None:
    if len(list_to_sort) <= 1:
        return list_to_sort

    more_list = []
    equal_list = []
    less_list = []

    pivot_element = list_to_sort[len(list_to_sort) // 2]

    for element in list_to_sort:
        if element > pivot_element:
            more_list.append(element)
        elif element < pivot_element:
            less_list.append(element)
        elif element == pivot_element:
            equal_list.append(element)

    return quick_sort(less_list) + equal_list + quick_sort(more_list)
