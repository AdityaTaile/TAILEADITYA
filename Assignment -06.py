# to be added loot, see add_to_inventory function (given as list in the assignment)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# starting inventory (given as dictionary in the assignment)
inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}


# function to print inventory, including total items no.
def display_inventory(lst):
    total_items = 0
    for i in lst:
        print(str(lst[i]) + " " + str(i))
        total_items += lst[i]
    print("Total number of items: " + (str(total_items)))


display_inventory(inventory)

# function to add new item set to inventory: The first part is to change the list of loot to a dictionary, the second is to either add the amount to the items already in inventory, or to add the key value pair altogether. The last part isto print current inventory just like the function before

# to get an empty space in the output
print


def add_to_inventory(inv, added_items):
    added_itemsQ = {}
    total_items = 0
    for item in added_items:
        added_itemsQ[item] = 1
    for i in added_itemsQ:
        if not i in inv:
            inv[i] = added_itemsQ[i]
        else:
            inv[i] = inv[i] + added_itemsQ[i]
    for i in inv:
        print(str(inv[i]) + " " + str(i))
        total_items += inv[i]
    print("Total number of items: " + (str(total_items)))


add_to_inventory(inventory, dragonLoot)
