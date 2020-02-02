from src.model.ItemList import ItemList
from src.model.ShoppingItem import ShoppingItem


class ItemListController:
    item_list: ItemList

    """
    ItemList Controller
    """

    def __init__(self, item_list_model: ItemList):
        self.item_list = item_list_model

    def add_item(self, item: ShoppingItem):
        """
        Adds given item to item list

        Args:
            item (ShoppingItem): given item
        """
        self.item_list.add_item(item)

    def add_items(self, *items: ShoppingItem):
        """
        Adds given items to item list

        Args:
            *items (ShoppingItem): given items
        """
        for item in items:
            self.add_item(item)
