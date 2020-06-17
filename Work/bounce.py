# bounce.py
#
# Exercise 1.5

import math as math

decay_rate = 0.6 # 3/5 of previous rate
initial_height = 100 # Height (meters)
bounce_threshold = 10
bounce_no = 1

while bounce_no <= bounce_threshold:
    print(bounce_no, round(initial_height * math.pow(decay_rate,bounce_no),4))
    bounce_no = bounce_no + 1

#print('Number of days', day)
#print('Number of bills', num_bills)
#print('Final height', num_bills * bill_thickness)