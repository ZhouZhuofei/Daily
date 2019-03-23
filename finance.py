def futureValue(p, r, m, t) :
    i = r / m
    n = m * t
    amount = p * ((1 + i) ** n)
    return amount
