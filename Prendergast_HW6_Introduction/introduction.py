"""
Braxton Prendergast
2/20/2025
HW6
Python Introduction
"""
#setting two numbers as variables
num1 = input("Give me an even number")
num2 = input("Give me another even number lower than the first")
#repeating the number to the user
print("Your numbers are", num1 , "and", num2 )
#arethmetic functions
sum = int(num1) + int(num2)
product = int(num1) * int(num2)
difference = int(num1) - int(num2)
quotient = int(num1) / int(num2)
all = int(sum) + int(difference) + int(product) + int(quotient)
#displaying to the user each value of their two numbers
print(f'{num1} + {num2} = {sum}')
print(f'{num1} - {num2} = {difference}')
print(f'{num1} * {num2} = {product}')
print(f'{num1} / {num2} = {quotient}')
print("That all adds up to: ", all)