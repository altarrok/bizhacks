from src.model.Chat import Chat
from src.model.ShoppingItem import ShoppingItem
from src.model.ItemList import ItemList
from src.model.VirtualAssistant import VirtualAssistant
from src.control.ChatController import ChatController
from src.control.BestBuyAPI import BestbuyClient
from src.control.ItemListController import ItemListController
from src.control.ShoppingItemController import ShoppingItemController
from src.control.VirtualAssistantController import VirtualAssistantController
from src.view.view import View
import time


def main():
    """
    Initial Models
    """
    virtual_assistant = VirtualAssistant()
    chat = Chat(virtual_assistant)
    item_list = ItemList()

    """
    Controllers
    """
    chat_controller = ChatController(chat)
    virtual_assistant_controller = VirtualAssistantController(
        virtual_assistant)
    item_list_controller = ItemListController(item_list)

    """
    View
    """
    view = View()

    """
    BestBuy API
    """
    bb_api = BestbuyClient("D2MdM7zQG5OJdzY61jyC0Fjm")

    """
    Runtime
    """

    def msgAction(event):
        input = view.input_field.get()
        view.pushChat(input + "\n")
        view.input_user.set("")
        virtual_assistant_controller.updateSearchQuery(input)
        r = bb_api.newSearch(virtual_assistant_controller.getSearchQuery())
        if (len(r) >= 3):
            view.changeLabel1("##" + r[0]['name'] + "##")
            view.changeLabel2(
                "##" + ("Price: " + str(r[0]['salePrice']) + "##"))
            view.changeLabel3("##" + "Rating: " +
                              str(r[0]["customerRating"]) + "##")

            view.changeLabel4("##" + r[1]['name'] + "##")
            view.changeLabel5("##" + "Price: " +
                              str(r[1]['salePrice']) + "##")
            view.changeLabel6("##" + "Rating: " +
                              str(r[1]["customerRating"]) + "##")

            view.changeLabel7("##" + r[2]['name'] + "##")
            view.changeLabel8("##" + "Price: " +
                              str(r[2]['salePrice']) + "##")
            view.changeLabel9("##" + "Rating: " +
                              str(r[2]["customerRating"]) + "##")
        view.pushChat(virtual_assistant_controller.getNextLine() + "\n")

    view.assign(msgAction)

    view.pushChat("Hello, I'm AKASIA. What would you like to buy today?\n")

    view.mainLoop()


if __name__ == "__main__":
    main()
