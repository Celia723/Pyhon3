import random
from typing import Generator, List, Tuple

# Definimos un alias de tipo para mayor claridad
Event = Tuple[str, str]


def gen_event() -> Generator[Event, None, None]:
    players: List[str] = ["bob", "alice", "dylan", "charlie"]
    list_action: List[str] = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]

    while True:
        name: str = random.choice(players)
        action: str = random.choice(list_action)
        yield (name, action)


def consume_event(events: List[Event]) -> Generator[Event, None, None]:
    while len(events) > 0:
        chosen: Event = random.choice(events)
        events.remove(chosen)
        yield chosen


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()   # ← crear el generador UNA vez

    # 1000 eventos
    for i in range(1000):
        tupla: Event = next(stream)
        print(f"Event {i}: Player {tupla[0]} did action {tupla[1]}")

    print()

    # lista de 10 eventos (tu forma original)
    tupla_list: List[Event] = []
    for i in range(10):
        tupla_list.append(next(stream))
    print(f"Built list of 10 events: {tupla_list}")

    # consumir la lista
    for delete in consume_event(tupla_list):
        print(f"Got event from list: {delete}")
        print(f"Remains in list: {tupla_list}")


