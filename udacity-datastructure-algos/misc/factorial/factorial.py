def factorial_calc(number):
    number_sum = number

    if number == 0:
        return 1

    while number > 1:
        number_sum = number_sum*(number - 1)
        number-= 1

    return number_sum