# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):

    if isinstance(x, int) and isinstance(y, int):
        if (x < 0 or x > 100) and (y < 0 or y > 100):
            "x must be between 0 and 100"
        else:
            return x + y

