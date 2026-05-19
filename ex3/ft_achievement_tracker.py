import random


def gen_player_achievements() -> set:
    ACHIEVEMENTS = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind",
        "Unstoppable", "Hidden Path Finder"
    ]
    n = random.randint(4, 8)
    return set(random.sample(ACHIEVEMENTS, n))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("Player Alice:", alice)
    print()
    print("Player Bob:", bob)
    print()
    print("Player Charlie:", charlie)
    print()
    print("Player Dylan:", dylan)
    print()

    all_ach = alice.union(bob, charlie, dylan)
    common = alice.intersection(bob, charlie, dylan)

    print("All distinct achievements:", all_ach)
    print()
    print("Common achievements:", common)

    print("Only Alice has:", alice.difference(bob, charlie, dylan))
    print("Only Bob has:", bob.difference(alice, charlie, dylan))
    print("Only Charlie has:", charlie.difference(alice, bob, dylan))
    print("Only Dylan has:", dylan.difference(alice, bob, charlie))
    print()
    print("Alice is missing:", all_ach.difference(alice))
    print("Bob is missing:", all_ach.difference(bob))
    print("Charlie is missing:", all_ach.difference(charlie))
    print("Dylan is missing:", all_ach.difference(dylan))
