def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        # 得到新的步长
        gap = gap // 2


def shell_sort_exercise(alist):
    n = len(alist)

    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i

            while j >= gap and alist[j] < alist[j - gap]:
                alist[j], alist[j - gap] = alist[j - gap], alist[j]
                j -= gap
        gap = gap // 2


alist = [54, 26, 93, 17, 77, 31, 19, 44, 55, 20]
shell_sort_exercise(alist)
print(alist)
