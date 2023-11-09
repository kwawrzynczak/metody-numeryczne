def horner(factors, f_len, x):
    result = factors[0]
    for i in range(1, f_len):
        result = result * x + factors[i]
    return result
