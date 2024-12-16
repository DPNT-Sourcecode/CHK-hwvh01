
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Prices for items
    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }

    # Initialize variables for counts and prices
    aPrice = bPrice = cPrice = dPrice = ePrice = fPrice = 0
    a = b = c = d = e = f = 0
    freeB = freeF = 0

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
                    # Apply special offer for 2 E's at 80
                    if e == 2:
                        ePrice -= 40  # Correct pricing for 2 E's
                        freeB += 1  # Free B with 2 E's
                        e = 0
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

    # Total cost calculation
    total_cost = aPrice + bPrice + cPrice + dPrice + ePrice + fPrice
    total_cost -= freeB * data['B']  # Subtract the cost of free B's
    total_cost -= freeF * data['F']  # Subtract the cost of free F's

    return total_cost






