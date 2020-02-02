class ItemList:
    item_list = []

    def __init__(self):
        self.item_list = []

    # Adds the shopping item into the item_list
    def add_item_list(self, shopping_item_add):
        self.item_list.append(shopping_item_add)

    # Removes the shopping item from the item_list
    def remove_item_list(self, shopping_item_remove):
        self.item_list.remove(shopping_item_remove)

    # Gets the item inside item list and prints it    ## change it
    def find_item(self, shopping_item_get):
        for ShoppingItem in self.item_list:
            if ShoppingItem == shopping_item_get:
                return shopping_item_get
