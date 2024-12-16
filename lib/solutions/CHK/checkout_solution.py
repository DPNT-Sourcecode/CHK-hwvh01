

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    aCount = int(0)
    bCount = int(0)
    cCount = int(0)
    dCount = int(0)
    eCount = int(0)

    cost = 0

    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    special_offers = {
        'A': [(3, 130), (5, 200)],  # 3 A's for 130, 5 A's for 200
        'B': [(2, 45)],  # 2 B's for 45
        'E': [(2, 80, 1)]  # 2 E's for 80 + 1 B free
    }

    for sku in skus:
        if isinstance(sku, str) and sku.isalpha():
            if sku not in data:
                return -1

            if sku == "A":
                aCount += 1
            elif sku == "B":
                bCount += 1
            elif sku == "C":
                cCount += 1
            elif sku == "D":
                dCount += 1
            elif sku == "E":
                eCount += 1
        else:
            return -1

    if aCount >= 5:
        offer_count = aCount // 5
        cost += offer_count * special_offers['A'][0][1]
        aCount %= 5

    if aCount >= 3:
        offer_count = bCount // 3
        cost += offer_count * special_offers['A'][1][1]
        bCount %= 3

    cost += aCount * data['A']

    if bCount >= 2:
        offer_count = bCount // 2
        cost += offer_count * special_offers['B'][0][1]
        bCount %= 2

    if eCount >= 2:
        offer_count = eCount // 2
        cost += offer_count * special_offers['E'][0][1]
        bCount += offer_count
        eCount %= 2

    cost += bCount * data['B']
    cost += cCount * data['C']
    cost += dCount * data['D']
    cost += eCount * data['E']

    return cost






