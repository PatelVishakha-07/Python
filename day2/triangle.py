n = int(input("enter a no: "))

for i in range(n):
    c = 65
    for k in range(i,n):
        print("", end = " ")

    for j in range(0, i+1):
        print(chr(c), end = " ")
        c += 1
    print()
