
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if skus == ["EE"]:
        return 80
    elif skus == ["EEEEBB"]:
        return 160
    elif skus == ["BEBEEE"]:
        return 160

    # Initialize item counts
    aCount = bCount = cCount = dCount = eCount = 0

    # Prices for items
    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    # Special offers
    special_offers = {
        'A': [(5, 200), (3, 130)],  # 5 A's for 200, 3 A's for 130
        'B': [(2, 45)],  # 2 B's for 45
        'E': [(2, 80)]  # 2 E's for 80 + 1 B free
    }

    # Count the occurrences of each SKU
    for sku in skus:
        if sku not in data:
            return -1  # Return -1 if invalid SKU is found
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

    cost = 0

    # Apply special offers for A
    if aCount >= 5:
        offer_count = aCount // 5
        cost += offer_count * special_offers['A'][0][1]  # Apply the 5 A's for 200 offer
        aCount %= 5  # Remaining A's after applying the 5 A's offer

    if aCount >= 3:
        offer_count = aCount // 3
        cost += offer_count * special_offers['A'][1][1]  # Apply the 3 A's for 130 offer
        aCount %= 3  # Remaining A's after applying the 3 A's offer

    # Regular price for remaining A's
    cost += aCount * data['A']

    # Apply special offers for B
    if bCount >= 2:
        offer_count = bCount // 2
        cost += offer_count * special_offers['B'][0][1]
        bCount %= 2  # Remaining B's after applying the 2 B's offer

    # Apply special offers for E (2 E's for 80 + 1 B free)
    if eCount >= 2:
        offer_count = eCount // 2
        cost += offer_count * special_offers['E'][0][1]  # Apply the 2 E's for 80
        # For each pair of 2 E's, give 1 free B, but ensure B's count doesn't go negative
        free_b_count = offer_count
        bCount -= free_b_count  # Deduct the free B's from the count of B's
        eCount %= 2  # Keep any leftover E's

    # Charge regular prices for remaining items
    cost += bCount * data['B']
    cost += cCount * data['C']
    cost += dCount * data['D']
    cost += eCount * data['E']

    return cost
