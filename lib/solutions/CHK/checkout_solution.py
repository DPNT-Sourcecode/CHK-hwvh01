
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
        if isinstance(skus[i], str) and skus[i].isalpha():
            if skus[i] in data:
                





    return cost



