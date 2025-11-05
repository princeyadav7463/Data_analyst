"""
Amount = P(1 + R/100) ** T
ci = Amount - P
"""

principal = float(input("Enter the principal amount "))
rate = float(input("Enter the rate "))
time = float(input("Enter the time "))
amount1 = principal * (1 + rate/100) ** time
amount2 = principal *pow((1 + rate/100), time)
print(amount1, amount2)