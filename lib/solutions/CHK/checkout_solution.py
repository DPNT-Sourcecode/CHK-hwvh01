
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

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    freeB = 0
    freeF = 0

    offset = 0

    # Prices for items
    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }

    # Special offers
    special_offers = {
        'A': [(5, 200), (3, 130)],  # 5 A's for 200, 3 A's for 130
        'B': [(2, 45)],  # 2 B's for 45
        'E': [(2, 80)],
        'F': [(3, 20)]
    }

    for i in range(0, len(skus)):
        if isinstance(skus[i], str) and skus[i].isalpha() and skus[i].capitalize():
            if skus[i] in data:
                match skus[i]:
                    case 'A':
                        a += 1
                        aPrice += data[skus[i]]
                        if a == 3:
                            aPrice -= 20
                        if a == 5:
                            aPrice -= 30
                            a = 0
                    case 'B':
                        b += 1
                        bPrice += data[skus[i]]
                        if b == 2:
                            bPrice -= 15
                            b = 0
                    case 'C':
                        c += 1
                        cPrice += data[skus[i]]
                    case 'D':
                        d += 1
                        dPrice += data[skus[i]]
                    case 'E':
                        e += 1
                        ePrice += data[skus[i]]
                        if e == 2:
                            ePrice += data[skus[i]]
                            freeB += data["B"]
                            e = 0
                    case 'F':
                        f += 1
                        fPrice += data[skus[i]]
                        if f == 3:  # This applies the new offer for F (3 Fs = 1 free)
                            freeF += data["F"]
                            f = 0
            else:
                return -1
        else:
            return -1
    cost = sum([aPrice, bPrice, cPrice, dPrice, ePrice, fPrice])
    cost -= freeB
    cost -= freeF
    return cost













