

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
            if sku not in data.keys():
                return -1
            else:


