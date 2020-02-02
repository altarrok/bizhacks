from src.model.VirtualAssistant import VirtualAssistant


class Chat:
    user_inputs = []  # User inputs so far
    assistant = None

    def __init__(self, assist):
        self.user_inputs = []
        self.assistant = assist

    def get_user_input_from_controller(self, user_input):  # Gets the user input and puts it in an array
        self.user_inputs.append(user_input)
        last_item = self.user_inputs[-1]
        self.assistant.update(last_item)

    def get_user_name(self, user_name):  # Get user's name
        self.user_inputs.append(user_name)
        self.assistant.greeting(user_name)

    def set_brand(self, brand):
        if brand == "No" or brand == "no":
            return
        self.user_inputs.append(brand)
        self.assistant.brand = brand

    def set_color(self, color):
        if color == "No" or color == "no":
            return
        self.user_inputs.append(color)
        self.assistant.color = color

    def set_max_price(self, max_price):
        if max_price == "No" or max_price == "no":
            return
        self.user_inputs.append(max_price)
        self.assistant.max_price = max_price
