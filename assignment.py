Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>  Personal Income Tax Calculator (2009)
... 
... status = int(input("Enter filing status (0=Single, 1=Married Jointly, 2=Married Separately, 3=Head of Household): "))
... income = float(input("Enter taxable income: "))
... 
... tax = 0
... 
... if status == 0:  # Single
...     brackets = [(8350, 0.10), (33950, 0.15), (82250, 0.25),
...                 (171550, 0.28), (372950, 0.33)]
... elif status == 1:  # Married filing jointly
...     brackets = [(16700, 0.10), (67900, 0.15), (137050, 0.25),
...                 (208850, 0.28), (372950, 0.33)]
... elif status == 2:  # Married filing separately
...     brackets = [(8350, 0.10), (33950, 0.15), (68525, 0.25),
...                 (104425, 0.28), (186475, 0.33)]
... elif status == 3:  # Head of household
...     brackets = [(11950, 0.10), (45500, 0.15), (117450, 0.25),
...                 (190200, 0.28), (372950, 0.33)]
... else:
...     print("Invalid filing status")
...     exit()
... 
... previous_limit = 0
... 
... for limit, rate in brackets:
...     if income > limit:
...         tax += (limit - previous_limit) * rate
...         previous_limit = limit
...     else:
...         tax += (income - previous_limit) * rate
...         break
... else:
...     tax += (income - previous_limit) * 0.35
... 
