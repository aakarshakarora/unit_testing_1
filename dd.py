import sys


def two_sum(lst, n, req):
    for i in range(n):
        for j in range(n):
            s = lst[i] + lst[j]
            if s == req:
                return 1

    return -1


lstArg = []
for arg in sys.argv:
    if arg == "dd.py":
        continue
    lstArg.append(int(arg))


n = lstArg[0]
nCheck = False
req = lstArg[-1]
lst = lstArg[1:len(lstArg)]
# while not nCheck:
#     try:
#         n = int(input("Enter Size of Array: "))
#
#         if isinstance(n, int):
#             nCheck = True
#         else:
#             print("Enter Proper Integer")
#
#     except ValueError:
#         print("Enter Proper Integer")
#
# for i in range(n):
#
#     inpCheck = False
#
#     while not inpCheck:
#         try:
#             inp = int(input("Enter Value at " + str(i) + " Index: "))
#             if isinstance(inp, int):
#                 inpCheck = True
#                 lst.append(inp)
#             else:
#                 print("Enter Valid Integer")
#         except ValueError:
#             print("Enter Valid Integer")
#
# reqCheck = False
#
# while not reqCheck:
#     try:
#         req = int(input("Enter Target Sum: "))
#
#         if isinstance(req, int):
#             reqCheck = True
#         else:
#             print("Enter Valid Integer")
#
#     except ValueError:
#         print("Enter Valid Integer")

print(two_sum(lst, n, req))
