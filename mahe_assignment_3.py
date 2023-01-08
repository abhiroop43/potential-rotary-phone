num = input("Enter the number of elements in the list: ")
fruits = []
apple_types = []

for i in range(int(num)):
    fruit = input("Enter your favorite fruits: ")
    fruits.append(fruit)

print(f"The elements in the fruits are: {fruits}")

for frt in fruits:
    if frt.upper().endswith("APPLE"):
        apple_types.append(frt)

print(f"The fruits that end with apples: {apple_types}")
