number = int(input("Enter a number for a multiplication table: "))
i = 1
print(f"Multiplication Table for {number}:")
print(f"Example of Tables:")

while i < 11:
    multiple = number * i
    print(f"{number} x {i} = {multiple}")
    i += 1