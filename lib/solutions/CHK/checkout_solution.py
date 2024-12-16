

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    aCount = int(0)
    bCount = int(0)

    cost = 0

    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    special_offers = {
        'A': (3, 130),  # 3 A's for 130
        'B': (2, 45)  # 2 B's for 45
    }

    for sku in skus:
        if isinstance(sku, str) and sku.isalpha():
            if sku not in data:
                return -1

            if sku == 'A':
                aCount += 1
            elif sku == 'B':
                bCount += 1
            elif sku == 'C':
                cost += data[sku]
            elif sku == 'D':
                cost += data[sku]
        else:
            return -1

    if aCount >= 3:
        offer_count = aCount // 3
        cost += offer_count * special_offers['A'][1]
        aCount %= 3

    if bCount >= 2:
        offer_count = bCount // 2
        cost += offer_count * special_offers['B'][1]
        bCount %= 2

    cost += aCount * data['A']
    cost += bCount * data['B']

    return cost



