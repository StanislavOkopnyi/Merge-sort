# Сортировка слиянием (англ. merge sort) — алгоритм сортировки,
# который упорядочивает списки (или другие структуры данных,
# доступ к элементам которых можно получать только последовательно,
# например — потоки) в определённом порядке.
# Эта сортировка — хороший пример использования принципа «разделяй и властвуй».
# Сначала задача разбивается на несколько подзадач меньшего размера.
# Затем эти задачи решаются с помощью рекурсивного вызова или непосредственно,
# если их размер достаточно мал.
# Наконец, их решения комбинируются, и получается решение исходной задачи.

def merge_sort(list_to_sort: list):
    if len(list_to_sort) > 1:
        half_list1 = merge_sort(list_to_sort[:len(list_to_sort) // 2])
        half_list2 = merge_sort(list_to_sort[len(list_to_sort) // 2:])

        index1, result = 0, []
        while index1 < len(half_list1):
            index2 = 0
            while index2 < len(half_list2):
                if half_list1[index1] > half_list2[index2]:
                    result.append(half_list2[index2])
                    half_list2.pop(index2)
                    index2 -= 1
                else:
                    result.append(half_list1[index1])
                    half_list1.pop(index1)
                    index1 -= 1
                    break
                index2 += 1
            index1 += 1

        if half_list2:
            result.extend(half_list2)
        elif half_list1:
            result.extend(half_list1)

        return result

    else:
        return list_to_sort
