from two_sum import two_sum

nCheck = False
n = 0
req = 0
lst = []
while not nCheck:
    try:
        n = int(input("Enter Size of Array: "))

        if isinstance(n, int):
            nCheck = True
        else:
            print("Enter Proper Integer")

    except ValueError:
        print("Enter Proper Integer")

for i in range(n):

    inpCheck = False

    while not inpCheck:
        try:
            inp = int(input("Enter Value at " + str(i) + " Index: "))
            if isinstance(inp, int):
                inpCheck = True
                lst.append(inp)
            else:
                print("Enter Valid Integer")
        except ValueError:
            print("Enter Valid Integer")

reqCheck = False

while not reqCheck:
    try:
        req = int(input("Enter Target Sum: "))

        if isinstance(req, int):
            reqCheck = True
        else:
            print("Enter Valid Integer")

    except ValueError:
        print("Enter Valid Integer")

print(two_sum(lst, n, req))
