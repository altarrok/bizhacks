class VirtualAssistant:
    last_search_query = ""
    brand = None
    color = None
    max_price = None

    def __init__(self):
        self.last_search_query = ""

    def update(self, last_item):  # Update the last search query
        self.last_search_query = last_item + " " + self.last_search_query

    def get_last_search(self):  # Get the last search query
        return self.last_search_query

    def greeting(self):  # Greet user with their name
        return "What do you want to use the laptop for?"

    def fetching_results(self, search_query):
        return "Alright, I'm fetch  ing all the " + search_query + ". Just a second please"

    def ask_brand(self):
        return "What screen size of laptop do you want (inches)?"

    def ask_color(self):
        return "What brand of laptop do you want?"

    def ask_max_price(self):
        return "Are you satisfied with your results?"
