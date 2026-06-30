n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))

op = input("enter operator [+, -, *, /, %]: ")

if op == "+":
    print(f"{n1} {op} {n2} = { n1 + n2}")
elif op == "-":
    print(f"{n1} {op} {n2} = { n1 - n2}")
elif op == "*":
    print(f"{n1} {op} {n2} = { n1 * n2}")
elif op == "/":
    print(f"{n1} {op} {n2} = { n1 / n2}")
elif op == "%":
    print(f"{n1} {op} {n2} = { n1 % n2}")
else:
    print("Invalid Choice...")
