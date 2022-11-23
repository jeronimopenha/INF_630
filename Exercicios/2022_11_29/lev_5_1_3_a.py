def dc_pow(base: int, expoente: int) -> int:
    if expoente == 1:
        return base

    if expoente % 2 == 0:
        t = dc_pow(base, expoente//2)
        t = t*t
        return t
    else:
        t = dc_pow(base, (expoente-1)//2)
        t = base*t*t
        return t


print(dc_pow(2, 13))
