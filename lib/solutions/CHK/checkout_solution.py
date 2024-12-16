
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Price table for items
    data = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }

    # Special offers: (how many items, price for those items)
    special_offers = {
        'A': [(5, 200), (3, 130)],  # 5 A's for 200, 3 A's for 130
        'B': [(2, 45)],  # 2 B's for 45
        'E': [(2, 80)],  # 2 E's for 80 + 1 B free
        'F': [(3, 20)]   # 2 F's for 10, buy 3 F's, pay for 2
    }

    # Initialize item counts
    a = b = c = d = e = f = 0

    # Parse the skus string and count occurrences
    for sku in skus:
        if sku not in data:
            return -1  # Return -1 if there's any invalid SKU
        if sku == 'A':
            a += 1
        elif sku == 'B':
            b += 1
        elif sku == 'C':
            c += 1
        elif sku == 'D':
            d += 1
        elif sku == 'E':
            e += 1
        elif sku == 'F':
            f += 1

    total_cost = 0
    free_b = free_f = 0  # Track free items due to special offers

    # Apply special offers for A (5 A's for 200, 3 A's for 130)
    if a >= 5:
        offer_count = a // 5
        total_cost += offer_count * special_offers['A'][0][1]  # 5 A's for 200
        a %= 5  # Remaining A's after applying the 5 A's offer
    if a >= 3:
        offer_count = a // 3
        total_cost += offer_count * special_offers['A'][1][1]  # 3 A's for 130
        a %= 3  # Remaining A's after applying the 3 A's offer
    # Regular price for remaining A's
    total_cost += a * data['A']

    # Apply special offers for B (2 B's for 45)
    if b >= 2:
        offer_count = b // 2
        total_cost += offer_count * special_offers['B'][0][1]  # 2 B's for 45
        b %= 2  # Remaining B's after applying the 2 B's offer
    # Regular price for remaining B's
    total_cost += b * data['B']

    # Apply special offers for E (2 E's for 80 + 1 B free)
    if e >= 2:
        offer_count = e // 2
        total_cost += offer_count * special_offers['E'][0][1]  # 2 E's for 80
        # For each pair of 2 E's, get 1 B free, but ensure B's count doesn't go negative
        free_b += offer_count
        e %= 2  # Remaining E's after applying the 2 E's offer
    # Regular price for remaining E's
    total_cost += e * data['E']

    # Apply special offers for F (Buy 2 F's, get 1 F free)
    if f >= 3:
        offer_count = f // 3
        total_cost += offer_count * special_offers['F'][0][1]  # 3 F's for 20
        free_f += offer_count  # Track how many F's are free
        f %= 3  # Remaining F's after applying the offer
    # Regular price for remaining F's
    total_cost += f * data['F']

    # Apply any free B's and F's
    total_cost -= free_b * data['B']  # Subtract free B's from total cost
    total_cost -= free_f * data['F']  # Subtract free F's from total cost

    # Apply regular prices for C and D (no special offers for these items)
    total_cost += c * data['C']
    total_cost += d * data['D']

    return total_cost







