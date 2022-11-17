import math


def calc_math_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == ":" and num2 == 0:
        return None
    elif operator == ":":
        return num1 / num2
    else:
        return None


def calc_math_expression_from_str(str_input):
    param = str_input.split(" ")
    num1 = float(param[0])
    num2 = float(param[2])
    operator = param[1]
    return calc_math_expression(num1, num2, operator)


def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    if (num1 <= num2) and (num1 <= num3):
        smallest = num1
    elif (num2 <= num1) and (num2 <= num3):
        smallest = num2
    else:
        smallest = num3

    return largest, smallest


def quadratic_equation_solver(a, b, c):
    if a == 0:
        return "Invalid a value, please check equation"
    disc = (b**2) - (4 * a * c)
    sqrt_val = math.sqrt(abs(disc))
    if disc > 0:
        val1 = (-b + sqrt_val)/(2 * a)
        val2 = (-b - sqrt_val)/(2 * a)
        return val1, val2
    elif disc == 0:
        val1 = -b / (2 * a)
        return val1, None
    else:
        return None, None


def quadratic_equation_solver_from_user_input():
    inp_str = input("Give me three numbers split by spaces, friend! ")
    lst = inp_str.split(" ")
    return quadratic_equation_solver(lst[0], lst[1], lst[2])


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 > min_temp and temp_2 > min_temp:
        return True
    elif temp_2 > min_temp and temp_3 > min_temp:
        return True
    elif temp_1 > min_temp and temp_3 > min_temp:
        return True
    else:
        return False
