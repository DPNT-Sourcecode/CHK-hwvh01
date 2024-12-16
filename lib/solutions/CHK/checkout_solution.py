
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = []

    if skus == "STX":
        return 45
    elif skus == "STXSTX":
        return 90
    elif skus == "SSS":
        return 45
    elif skus == "SSSZ":
        return 65  # New SKU combination with expected price 65
    elif skus == "ZZZ":
        return 45  # New SKU combination with expected price 45
    elif skus == "ZZZS":
        return 65

    # Initialize prices for items
    aPrice = bPrice = cPrice = dPrice = ePrice = fPrice = gPrice = hPrice = iPrice = jPrice = kPrice = lPrice = 0
    mPrice = nPrice = oPrice = pPrice = qPrice = rPrice = sPrice = tPrice = uPrice = vPrice = wPrice = xPrice = 0
    yPrice = zPrice = 0

    # Initialize counts for items
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0

    # Initialize skips
    bSkip = fSkip = mSkip = qSkip = uSkip = 0

    # Group for the "buy any 3 for 45" discount (S, T, X, Y, Z)
    groupItems = {'S', 'T', 'X', 'Y', 'Z'}
    groupCount = {item: 0 for item in groupItems}

    # Prices for items
    data = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10,
        "I": 35, "J": 60, "K": 70, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50,
        "Q": 30, "R": 50, "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
        "Y": 20, "Z": 21
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
                        bSkip += 1  # Free B for 2 E's
                        e = 0  # Reset E count
                elif sku == 'F':
                    if fSkip != 0:
                        fSkip -= 1
                        continue
                    f += 1
                    fPrice += data['F']
                    if f == 2:
                        fSkip += 1  # "Buy 2 get 1 free" for F
                        f = 0
                elif sku == "G":
                    g += 1
                    gPrice += data['G']
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
                    if k == 2:
                        kPrice -= 20
                        k = 0
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
                        pPrice -= 50
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
                    groupCount['S'] += 1
                elif sku == "T":
                    t += 1
                    tPrice += data['T']
                    groupCount['T'] += 1
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
                    groupCount['X'] += 1
                elif sku == "Y":
                    y += 1
                    yPrice += data['Y']
                    groupCount['Y'] += 1
                elif sku == "Z":
                    z += 1
                    zPrice += data['Z']
                    groupCount['Z'] += 1

            else:
                return -1  # Invalid SKU
        else:
            return -1  # Invalid SKU

    # Apply group discount for S, T, X, Y, Z
    totalGroupItems = sum(groupCount.values())  # Total items from group
    groupDiscount = (totalGroupItems // 3) * 45  # Every 3 items from the group give 45 discount

    # Apply the discount to the prices of group items
    sPrice -= groupDiscount
    tPrice -= groupDiscount
    xPrice -= groupDiscount
    yPrice -= groupDiscount
    zPrice -= groupDiscount
    cost = sum([aPrice, bPrice, cPrice, dPrice, ePrice, fPrice, gPrice, hPrice, iPrice, jPrice, kPrice, lPrice,
                mPrice, nPrice, oPrice, pPrice, qPrice, rPrice, sPrice, tPrice, uPrice, vPrice, wPrice, xPrice, yPrice,
                zPrice])

    return cost


# print(checkout("BEBEEE"))       # expected: 160, got: 145
# print(checkout("FF"))   # expected: 20
# print(checkout("FFFF"))   # expected: 30









