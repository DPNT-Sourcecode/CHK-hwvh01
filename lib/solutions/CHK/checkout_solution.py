
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

    for sku in skus:
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
                        freeB += 30  # Add free B (as 2 E's give 1 free B)
                        e = 0  # Reset E count after the offer
                elif sku == 'F':
                    f += 1
                    fPrice += data['F']
                    if f == 3:  # "Buy 2 get 1 free" for F
                        freeF += 1
                        f = 0
            else:
                return -1  # Invalid SKU
        else:
            return -1  # Invalid SKU
    cost = sum([aPrice, bPrice, cPrice, dPrice, ePrice, fPrice])
    cost -= freeB
    cost -= freeF
    return cost











