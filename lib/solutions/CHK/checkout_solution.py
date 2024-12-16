

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    aCount = int(0)
    bCount = int(0)

    current = ['a', 'b', 'c', 'd']

    for sku in skus:
        if isinstance(sku, str) and sku.isalpha():
            if sku not in current:
                return -1
            else:
                if
