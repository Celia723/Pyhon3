import random
from typing import List, Dict


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()

    players: List[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")
    print()

    # Lista con todos capitalizados (tu estilo)
    players_capitalize: List[str] = []
    for name in players:
        players_capitalize.append(name.capitalize())
    print(f"New list with all names capitalized: {players_capitalize}")
    print()

    # Lista con solo los que ya estaban capitalizados
    capitalize_only: List[str] = []
    for name in players:
        if name == name.capitalize():
            capitalize_only.append(name)
    print(f"New list of capitalized names only: {capitalize_only}")
    print()

    # Diccionario de puntuaciones
    score_dict: Dict[str, int] = {
        name: random.randint(0, 1000) for name in players_capitalize
    }
    print(f"Score dict: {score_dict}")

    average: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average: {average}")

    high_scores: Dict[str, int] = {
        name: score for name, score in score_dict.items() if score > average
    }
    print(f"High scores: {high_scores}")