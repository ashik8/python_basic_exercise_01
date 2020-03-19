"""
Write a program that will take hours and rate per hour as input and will compute the total payment.

Example:
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

"""

# take hours and rate as input
hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate:'))
pay = 0


# your code here
pay= hours*rate


print('Pay: {:.2f}'.format(pay))
