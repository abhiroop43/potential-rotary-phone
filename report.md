**Name:** Abhiroop Santra

**Batch:** Msc. DS

**Roll Number:** 22154090036


### Q1

```python
def calculate_water_bill(units):
    if units <= 100:
        billable_units = 0
        bill_amount = billable_units * 0
    elif 100 < units <= 200:
        billable_units = units - 100
        bill_amount = billable_units * 5
    else:
        over_200 = units - 200
        over_100_below_200 = units - (over_200 + 100)
        bill_amount = (over_200 * 10) + (over_100_below_200 * 5)

    return bill_amount


billed_units = input("Enter billed units: ")
print(f"Total billed amount is {calculate_water_bill(int(billed_units))}")

```

### Q2

```python
test = [print(i) for i in range(100) if i % 5 == 0]

```

### Q3

```python
num = input("Enter the number of elements in the list: ")
fruits = []
apple_types = []

for i in range(int(num)):
    fruit = input("Enter your favorite fruits: ")
    fruits.append(fruit)

print(f"The elements in the fruits are: {fruits}")

```

### Q4

```python
for frt in fruits:
    if frt.upper().endswith("APPLE"):
        apple_types.append(frt)

print(f"The fruits that end with apples: {apple_types}")

```

### Q5

```python
shopping_bill = {"apple": 5.00, "pineapple": 5.50, "grapes": 9.50}

print(f"Shopping Bill Details: {shopping_bill}")
print(f"Total Bill Amount: {sum(shopping_bill.values())}")

```

### Q6

```python
import pandas as pd

# 6a
df = pd.read_csv('./data/cereal.csv')

# 6b
honey_df = df[df["name"].str.contains("Honey")]
print(honey_df)

# 6c
honey_rice_df = df[(df["name"].str.contains("Honey") | df["name"].str.contains("Rice"))]
print(honey_rice_df)

```