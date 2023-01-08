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
