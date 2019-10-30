inventory = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12,

}

dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def invent(dictionary):
    print("Inventory:")
    total_value = 0
    for k, v in sorted(dictionary.items()):
        print(f"{v} {k}")
        total_value += v
    print(f"Total number of items : {total_value}")


def add_to_inventory(dictionary, added_items):
    for k in added_items:
        dictionary.setdefault(k, 0)
        dictionary[k] += 1
    return invent(dictionary)


print(add_to_inventory(inventory, dragon_loot))
