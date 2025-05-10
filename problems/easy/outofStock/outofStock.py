def inventoryFiller(inventory, required):
    """
    Filters out the required items from the inventory.

    Parameters:
    inventory (list): The list of available items in the inventory.
    required (list): The list of items to be removed from the inventory.

    Returns:
    list: The updated inventory after removing the required items.
    """
    for item in required:
        if item in inventory:
            inventory.remove(item)
    return inventory

# Test cases
inventory = ["apple", "banana", "orange", "grape"]
required = ["banana", "grape"]

print(inventoryFiller(inventory, required))  # ➞ ["apple", "orange"]

inventory = ["laptop", "mouse", "keyboard", "monitor"]
required = ["mouse", "keyboard"]

print(inventoryFiller(inventory, required))  # ➞ ["laptop", "monitor"]
