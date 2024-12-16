
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    basket = []

    aPrice = 0
    bPrice = 0
    cPrice = 0
    dPrice = 0
    ePrice = 0
    fPrice = 0
    gPrice = 0
    hPrice = 0
    iPrice = 0
    jPrice = 0
    kPrice = 0
    lPrice = 0
    mPrice = 0
    nPrice = 0
    oPrice = 0
    pPrice = 0
    qPrice = 0
    rPrice = 0
    sPrice = 0
    tPrice = 0
    uPrice = 0
    vPrice = 0
    wPrice = 0
    xPrice = 0
    yPrice = 0
    zPrice = 0

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h, i, j, k, l, m, n, o, p, q, r, p, s, t, u, p, v, w, x, y, z = 0

    bSkip = 0
    fSkip = 0
    mSkip = 0
    qSkip = 0
    uSkip = 0

    freeB = 0
    freeF = 0

    # Prices for items
    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }
    skusort = sorted(skus, reverse=True)
    for sku in skusort:
        if isinstance(sku, str) and sku.isalpha() and sku.capitalize():
            if sku in data:
                # Apply the offers based on the item
                if sku == 'A':
                    a += 1
                    aPrice += data['A']
                    if a == 3:
                        aPrice -= 20  # Discount for 3 A's
                    if a == 5:
                        aPrice -= 30  # Discount for 5 A's
                        a = 0
                elif sku == 'B':
                    if bSkip != 0:
                        bSkip -= 1
                        continue
                    b += 1
                    bPrice += data['B']
                    if b == 2:
                        bPrice -= 15  # Discount for 2 B's
                        b = 0
                elif sku == 'C':
                    c += 1
                    cPrice += data['C']
                elif sku == 'D':
                    d += 1
                    dPrice += data['D']
                elif sku == 'E':
                    e += 1
                    ePrice += data['E']
                    # When 2 E's are encountered, apply the offer
                    if e == 2:
                        # freeB += 30  # Add free B (as 2 E's give 1 free B)
                        bSkip += 1
                        e = 0  # Reset E count after the offer
                elif sku == 'F':
                    if fSkip != 0:
                        fSkip -= 1
                        continue
                    f += 1
                    fPrice += data['F']
                    if f == 2:  # "Buy 2 get 1 free" for F
                        fSkip += 1
                        f = 0
                elif sku == "H":
                    h += 1
                    hPrice += data['H']
                    if h == 5:
                        hPrice -= 5
                    if h == 10:
                        hPrice -= 15
                        h = 0
                elif sku == "I":
                    i += 1
                    iPrice += data['I']
                elif sku == "J":
                    j += 1
                    jPrice += data['J']
                elif sku == "K":
                    k += 1
                    kPrice += data['K']
                elif sku == "L":
                    l += 1
                    lPrice += data['L']
                elif sku == "M":
                    if mSkip != 0:
                        mSkip -= 1
                        continue
                    m += 1
                    mPrice += data['M']
                elif sku == "N":
                    n += 1
                    nPrice += data['N']
                    if n == 3:
                        mSkip += 1
                        n = 0
                elif sku == "O":
                    o += 1
                    oPrice += data['O']
                elif sku == "P":
                    p += 1
                    pPrice += data['P']
                    if p == 5:
                        pPrice -= 25
                        p = 0
                elif sku == "Q":
                    if qSkip != 0:
                        qSkip -= 1
                        continue
                    q += 1
                    qPrice += data['Q']
                    if q == 3:
                        qPrice -= 10
                        q = 0
                elif sku == "R":
                    r += 1
                    rPrice += data['R']
                    if r == 3:
                        qSkip += 1
                        r = 0
                elif sku == "S":
                    s += 1
                    sPrice += data['S']
                elif sku == "T":
                    t += 1
                    tPrice += data['T']
                elif sku == "U":
                    if uSkip != 0:
                        uSkip -= 1
                        continue
                    u += 1
                    uPrice += data['U']
                    if u == 3:
                        uSkip += 1
                        u = 0
                elif sku == "V":
                    v += 1
                    vPrice += data['V']
                    if v == 2:
                        vPrice -= 10
                    if v == 3:
                        vPrice -= 10
                        v = 0
                elif sku == "W":
                    w += 1
                    wPrice += data['W']
                elif sku == "X":
                    x += 1
                    xPrice += data['X']
                elif sku == "Y":
                    y += 1
                    yPrice += data['Y']
                elif sku == "Z":
                    z += 1
                    zPrice += data['Z']

            else:
                return -1  # Invalid SKU
        else:
            return -1  # Invalid SKU
    cost = sum([aPrice, bPrice, cPrice, dPrice, ePrice, fPrice])
    if bPrice != 0:
        print("free b ", freeB)
        cost -= freeB
    if fPrice != 0:
        cost -= freeF
    return cost


# print(checkout("BEBEEE"))       # expected: 160, got: 145
# print(checkout("FF"))   # expected: 20
# print(checkout("FFFF"))   # expected: 30



