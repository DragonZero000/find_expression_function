from itertools import product

def find_expressions(digits, target):
    result = []
    for operations in product(["+", "-", ""], repeat=len(digits) - 1):
        expr = digits[0]
        for oper, d in zip(operations, digits[1:]):
            expr += oper + d
        total_sum = 0
        sign = 1
        num = ""
        for ch in expr:
            if ch in "+-":
                total_sum += sign * int(num)
                if ch == "+":
                    sign = 1
                else:
                    sign = -1
                num = ""
            else:
                num += ch
        total_sum += sign * int(num)
        if total_sum == target:
            result.append(expr)
    return result

for expr in find_expressions("9876543210", 200):
    print(f"{expr}=200")