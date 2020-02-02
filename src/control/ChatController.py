from typing import *
from src.model.Chat import Chat


class ChatController:
    chat: Chat

    """
    Chat Controller
    """

    def __init__(self, chat_model: Chat):
        self.chat = chat_model

    def user_input(self, input: str):
        """
        Pushes user input to chat and returns the ## NOT SURE ## response of the virtual assistant

        Args:
            input (str): User Input
        """
        self.chat.user_input(input)
