current_savings = 0.0
r = 0.04

annual_salary = float(input("What is your annual salary?"))
portion_saved = float(input("How much are you saving per month?"))
total_cost = float(input("What's the cost of your dream home?"))

portion_down_payment = 0.25 * total_cost

monthly_salary = annual_salary / 12

monthly_saving = monthly_salary * portion_saved

n = 0
while current_savings < portion_down_payment:
    current_savings += monthly_saving + ((current_savings * r) /12)
    n += 1

print(n)
