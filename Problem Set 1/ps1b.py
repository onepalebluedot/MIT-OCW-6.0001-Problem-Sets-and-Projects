current_savings = 0.0
r = 0.04 #interest rate

annual_salary = float(input("What is your annual salary?"))
portion_saved = float(input("How much are you saving per month?"))
total_cost = float(input("What's the cost of your dream home?"))
semi_annual_raise = float(input("Enter a semi-annual salary raise as a decimal percentage"))

#raise should happen only AFTER the 6th month, 12th month, and so on

portion_down_payment = 0.25 * total_cost

monthly_salary = annual_salary / 12

monthly_saving = monthly_salary * portion_saved

# n is number of month
n = 0
while current_savings < portion_down_payment:
    current_savings += monthly_saving + ((current_savings * r) /12) # += is an operation that adds the two values together then assign the result to a variable. While monthly savings is consistent, current savings is growing by the month. 
    n += 1 # adding the number of month needed until current savings is great than required down payment

    if n % 6 == 0: #returns TRUE for every 6 months
        annual_salary += annual_salary * semi_annual_raise # a += 1 # a = a + 1
        monthly_saving = (annual_salary / 12) * portion_saved

print(n)
