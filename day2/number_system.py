
n = int(input("enter a no: "))

while True:
    ch = int(input("""
1. Decimal to Binary
2. Decimal to Octal
3. Decimal to Hexadecimal
9. Exit
Enter your choice: """))
    
    if ch == 1:
        print(f"{n} in binary: {bin(n)}")

    elif ch == 2:
        print(f"{n} in octal: {oct(n)}")

    elif ch == 3:
        print(f"{n} in hexadecimal: {hex(n)}")

    elif ch == 9:
        print("Good Bye")
        break
    
    else:
        print("invalid Choice...")
