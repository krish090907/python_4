a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))
p = 1
for i in range(b):
    p = p*a
print(f"{a} raised to the power {b} is: {p}")
