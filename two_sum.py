def two_sum(lst, n, req):
    for i in range(n):
        for j in range(n):
            s = lst[i] + lst[j]
            if s == req:
                return 1

    return -1
