"""
Simple interest = (P * R * T)/100
p = principal amount
r = rate of interest
t = time of interest
"""

principal = float(input("Enter the principal amount "))
rate = float(input("Enter the rate of interest "))
time = float(input("Enter the time of interest "))
si = (principal * rate * time) / 100
print("Simple interest = ",si)