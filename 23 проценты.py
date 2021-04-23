def calc_savings(s, i, t):
    print(s, i, t)
    for j in range(t):
        s += s * (i / 100)
        print(int(s))
    return s



s = 10000
i = 2
t = 2
calc_savings(s, i, t)
