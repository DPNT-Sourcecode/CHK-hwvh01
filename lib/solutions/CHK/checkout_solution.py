from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Prices for individual items
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

    # Special offers
    offers = {
        'A': [(3, 130), (5, 200)],
        'B': [(2, 45)],
        'E': [(2, 0)]  # 2E get 1B free
    }

    # Count the number of each SKU in the input string
    sku_count = Counter(skus)

    # Check for any invalid SKU
    if any(sku not in prices for sku in sku_count):
        return -1

    total_price = 0

    # Process each item in the basket
    for item, count in sku_count.items():
        if item == 'A':
            # Apply the best offer for A
            price = 0
            for quantity, offer_price in offers['A']:
                num_bundles = count // quantity
                price += num_bundles * offer_price
                count -= num_bundles * quantity
            # For remaining items, charge at regular price
            price += count * prices['A']
            total_price += price

        elif item == 'B':
            # Apply the best offer for B
            price = 0
            for quantity, offer_price in offers['B']:
                num_bundles = count // quantity
                price += num_bundles * offer_price
                count -= num_bundles * quantity
            # For remaining items, charge at regular price
            price += count * prices['B']
            total_price += price

        elif item == 'E':
            # Apply the special offer for E
            price = 0
            if count >= 2:
                # Bundle 2E and get 1B free
                num_bundles = count // 2
                price += num_bundles * (2 * prices['E'])  # 2 E's at regular price
                count -= num_bundles * 2
                # For each bundle, we get 1 free B, so adjust B's count
                sku_count['B'] += num_bundles

            # For remaining items, charge at regular price
            price += count * prices['E']
            total_price += price

        else:
            # For items C and D, charge at regular price
            total_price += count * prices[item]

    # Now, process item B because the offer may have changed its count due to E's offer
    if 'B' in sku_count:
        count = sku_count['B']
        price = 0
        for quantity, offer_price in offers['B']:
            num_bundles = count // quantity
            price += num_bundles * offer_price
            count -= num_bundles * quantity
        price += count * prices['B']
        total_price += price

    return total_price







