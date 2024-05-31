import heapq

def merge_k_lists(lists : list) -> list:

    total_list = []
    result_list =[]

    for ilist in lists:
        total_list.extend(ilist)

    heapq.heapify(total_list)

    while total_list:
        result_list.append(heapq.heappop(total_list))

    return result_list
    # за такої реалізації неважливо, чи будуть списки у списку сортовані (з точки зору алгоритму).
    # Можливо буде швидше працювати, якщо будуть посортовані, але складність створення купи все одно буде On.

lists = [[1, 4, 5], [1, 3, 4], [2, 6, 8, 11]]
print("Невідсортовані списки:", lists)
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
