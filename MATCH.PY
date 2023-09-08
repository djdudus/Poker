from random import randint
from collections import Counter
import itertools
from dicts import colors, values, hands


players = 4
# player = [player[i] for i in players]


def draw_card(amount, result=None):
    if result is None:
        result = []
    for i in range(amount):
        x = randint(0, 3)
        y = randint(0, 12)
        card = {"value": values[y], "color": colors[x]}
        if card not in result:
            result.append(card)
        else:
            amount = amount - i
            return draw_card(amount, result)
    return result


def get_card_value(card):
    return next(key for key, value in values.items() if value == card["value"])


def get_hand_value(hand):
    card_values = [get_card_value(card) for card in hand]
    card_colors = [card["color"] for card in hand]

    if len(set(card_colors)) == 1:
        if max(card_values) == values[12] and min(card_values) == values[10]:
            return 9
        elif max(card_values) - min(card_values) == 4:
            return 8
        else:
            return 6
    # STRIT (pięć kolejnych wartości kart)
    if (len(set(card_values)) == 5 and max(card_values) - min(card_values) == 4) or set(
        card_values
    ) == {0, 1, 2, 3, 12}:
        return 5

    card_values_counts = [card_values.count(value) for value in set(card_values)]
    if 4 in card_values_counts:
        return 7  # Kareta (cztery jednakowe wartości kart)
    elif set(card_values_counts) == {2, 3}:
        return 4  # Full (trójka i para)
    elif 3 in card_values_counts:
        return 3  # Trójka (trzy jednakowe wartości)
    elif card_values_counts.count(2) == 2:
        return 2  # Dwie pary
    elif card_values_counts.count(2) == 1:
        return 1  # Para.
    else:
        return 0  # Wysoka karta.


def compare_player_values(h1, h2, h3, h4):
    combinations = itertools.combinations(h1, 5)
    player1_values = [get_hand_value(combination) for combination in combinations]

    combinations = itertools.combinations(h2, 5)
    player2_values = [get_hand_value(combination) for combination in combinations]

    combinations = itertools.combinations(h3, 5)
    player3_values = [get_hand_value(combination) for combination in combinations]

    combinations = itertools.combinations(h4, 5)
    player4_values = [get_hand_value(combination) for combination in combinations]
    max_values = [
        max(player1_values),
        max(player2_values),
        max(player3_values),
        max(player4_values),
    ]
    winner = max_values.index(max(max_values)) + 1
    if max_values.count(max(max_values)) > 1:
        return "Tie!"
    else:
        return f"Player {winner} wins!"


def play_poker():
    card_pool = draw_card(2 * players + 5)
    table_cards = [
        card_pool[8],
        card_pool[9],
        card_pool[10],
        card_pool[11],
        card_pool[12],
    ]
    player1 = [
        card_pool[0],
        card_pool[1],
    ]
    player2 = [
        card_pool[2],
        card_pool[3],
    ]
    player3 = [
        card_pool[4],
        card_pool[5],
    ]
    player4 = [
        card_pool[6],
        card_pool[7],
    ]
    hand1 = table_cards + player1
    hand2 = table_cards + player2
    hand3 = table_cards + player3
    hand4 = table_cards + player4
    print(f"p1 {player1}")
    print(get_hand_value(hand1))
    print(f"p2 {player2}")
    print(get_hand_value(hand2))
    print(f"p3 {player3}")
    print(get_hand_value(hand3))
    print(f"p4 {player4}")
    print(get_hand_value(hand4))
    print(f"stół {table_cards}")
    # compare_player_values(get_hand_value(hand1),get_hand_value(hand2),get_hand_value(hand3),get_hand_value(hand4))
    print(compare_player_values(hand1, hand2, hand3, hand4))


play_poker()
