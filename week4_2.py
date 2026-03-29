n = int(input("Enter the range (upto n): "))
even = 0
odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Total even numbers from 1 to {n}: {even}")
print(f"Total odd numbers from 1 to {n}: {odd}")
