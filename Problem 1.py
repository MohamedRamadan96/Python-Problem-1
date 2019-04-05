# Question :- Accept two int values from user and return their product.
# If the product is greater than 1000, then return their sum ??
def display_my_product(number1 , number2):
    result = number1 * number2
    if result < 1000 :
        return result
    else:
        return number1 + number2

num1 = int(input('Enter The First Number ?'))
num2 = int(input('Enter The Second Number ?'))

num3 = display_my_product(num1,num2)
print('The Result is ', num3)