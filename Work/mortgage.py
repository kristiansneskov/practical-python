# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11 
total_paid = 0.0


extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000


month_count = 0

while principal > 0:
    month_count = month_count + 1
    if month_count >= extra_payment_start_month and month_count < extra_payment_end_month:
        monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment 
    if monthly_payment > principal:
        total_paid = total_paid + principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - monthly_payment
        total_paid = total_paid + monthly_payment
    print(f'{month_count} {(round(total_paid,2)):10.2f} {round(principal,2):10.2f}')

print(f'\nTotal paid {round(total_paid,2):14.2f}')
print(f'Number of months {month_count:8}')

