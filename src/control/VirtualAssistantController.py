from src.model.VirtualAssistant import VirtualAssistant


class VirtualAssistantController:
    virtual_assistant: VirtualAssistant

    """
    Virtual Assistant Controller
    """

    def __init__(self, virtual_assistant_model: VirtualAssistant):
        self.virtual_assistant = virtual_assistant_model
        self.i = 0

    def getNextLine(self) -> str:
        if self.i == 0:
            nextLine = self.virtual_assistant.greeting()
        elif self.i == 1:
            nextLine = self.virtual_assistant.ask_brand()
        elif self.i == 2:
            nextLine = self.virtual_assistant.ask_color()
        elif self.i == 3:
            nextLine = self.virtual_assistant.ask_max_price()
        else:
            nextLine = "I'm glad I could help"
        self.i += 1
        return nextLine

    def assignName(self, str):
        self.virtual_assistant.name = str

    def getSearchQuery(self):
        return self.virtual_assistant.last_search_query

    def updateSearchQuery(self, query):
        self.virtual_assistant.update(query)
