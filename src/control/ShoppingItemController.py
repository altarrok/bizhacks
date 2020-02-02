from src.model.ShoppingItem import ShoppingItem


class ShoppingItemController:
    shopping_item: ShoppingItem

    """
    Shopping Item Controller
    """

    def __init__(self, shopping_item_model: ShoppingItem):
        self.shopping_item = shopping_item_model
