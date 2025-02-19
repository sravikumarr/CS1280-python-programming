# Get user input
num = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication table of {num}:")

# Loop from 1 to 10 and print the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

