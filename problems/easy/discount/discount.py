from discount import getdiscountedPS

# p = original price
# d = percentage discount

def getdiscountedPS(p, d):
    """
    Calculate the final price after applying the discount.

    Parameters:
    p (float): The original price.
    d (float): The discount percentage.

    Returns:
    float: The final price rounded to two decimal places.
    """
    discounted_price = p * (1 - d / 100)
    return round(discounted_price, 2)

