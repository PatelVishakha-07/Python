a = 7
b = 5

print(f"Before Swap: a={a} b={b}")
a = a^b
b = a^b
a = a^b
print(f"After Swap: a={a} b={b}")