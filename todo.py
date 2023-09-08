# TODO:

# Dostosować funkcję compare_player_values do zmiennej ilości graczy


class Player:
    def __init__(self):
        self.hand = []
        self.money = 1000
        self.state = "inactive"


cards_on_table = []
current_cards = []


def fold():
    return 0


def uncover_cards(table_cards, qty):
    print("karty przed tobą:", table_cards[:qty])
